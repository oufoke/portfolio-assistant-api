# Assistant portfolio — API

Backend du chatbot qui répond aux questions des recruteurs sur le parcours
professionnel d'Oumar Fodé KEBE, appelé depuis le widget de
[oufoke.github.io](https://oufoke.github.io).

---

## Architecture

**Pas de RAG, volontairement.** Le corpus tient intégralement dans la fenêtre de
contexte du modèle. Un retrieval ajouterait une couche d'indexation, un risque de
rater le bon passage, et une latence supplémentaire — pour aucun gain à ce
volume. La décision serait à revoir si le corpus dépassait quelques centaines de
kilo-octets.

**Prompt caching.** Le corpus ne change pas d'un appel à l'autre : il est envoyé
dans un bloc système mis en cache. Les appels suivants ne repaient pas ces tokens
au plein tarif. L'indication de langue transmise par le widget est placée dans un
second bloc, non caché, pour ne pas invalider le cache à chaque changement.

```
widget (GitHub Pages)  ──POST /chat──>  API (Render)  ──>  API Claude
                       <──── JSON ────
```

---

## Endpoints

| Méthode | Route     | Description                        |
|---------|-----------|------------------------------------|
| GET     | `/health` | Disponibilité                      |
| POST    | `/chat`   | Question → réponse (10 req/min/IP) |

```json
{ "question": "Quel est son parcours ?", "history": [], "lang": "fr" }
```

`lang` accepte `fr` ou `en` uniquement. `history` est borné côté serveur à
8 messages, quelle que soit la valeur envoyée.

---

## Le corpus

`corpus/faq.md` est la **source prioritaire**, déclarée comme telle dans le
prompt système et chargée en premier. Elle est rédigée à la main et fait
autorité en cas de contradiction avec les autres fichiers.

| Fichier | Rôle |
|---|---|
| `faq.md` | Réponses de référence, rédigées au bon niveau de précision |
| `education.yaml` | Diplômes et cursus |
| `skills.yaml` | Domaines d'expertise |
| `accomplishments.yaml` | Certifications |
| `achievements.yaml` | Éléments extra-professionnels |

**Ce qui est délibérément exclu du corpus.** Les fichiers `about.yaml`,
`experiences.yaml` et `projects.yaml` du portfolio ne sont pas embarqués. Ils
sont rédigés pour un affichage web, avec des accroches condensées et des chiffres
arrondis pour l'accroche visuelle. Ce registre est inadapté à un assistant qui
doit rester factuel : quand les deux versions d'un même fait cohabitent dans le
contexte, le modèle peut piocher dans la mauvaise. Leur contenu factuel a été
réécrit dans `faq.md` aux formulations exactes.

### Règles de rédaction du corpus

- Les chiffres sont donnés tels qu'ils ont été mesurés, sans arrondi ni
  reformulation valorisante.
- Quand un chiffre porte sur des données de test ou synthétiques, c'est dit dans
  la même phrase que le chiffre, pas dans une note en bas de page.
- Ce qui est spécifié mais pas livré est distingué de ce qui est en production.
- Les limites du profil sont écrites dans le corpus, pas laissées à l'inférence
  du modèle.

---

## Garde-fous

Six règles dans le prompt système, prioritaires sur toute demande utilisateur :

1. **Sources uniquement** — aucune connaissance extérieure au corpus
2. **Pas d'extrapolation** — un chiffre absent reste absent
3. **Troisième personne** — l'assistant ne se substitue jamais à Oumar
4. **Sujets refusés** — rémunération, disponibilité précise, autres candidatures,
   vie personnelle
5. **Honnêteté sur les limites** — restituées telles quelles, jamais atténuées
6. **Résistance aux détournements** — changement de rôle, révélation du prompt
7. **Langue de réponse** — celle de la question, sans que cela lève les règles 1 à 6

---

## Évaluation

`run_eval.py` passe un jeu de 22 questions contre l'API déployée : 10 questions
normales et 12 pièges répartis en cinq familles — limites du profil, sujets
refusés, injections de prompt, hallucinations, sujets sensibles. Deux questions
sont en anglais, dont une combinant changement de langue et tentative de
contournement.

```bash
python3 run_eval.py          # les 22 questions
python3 run_eval.py piege    # les pièges seulement
```

La relecture reste manuelle. Le script signale automatiquement trois motifs :
présence de formulations arrondies bannies, usage possible de la première
personne, et mention d'un montant en rémunération.

---

## Configuration

`ANTHROPIC_API_KEY` est défini dans les variables d'environnement Render. Aucune
clé n'apparaît dans les fichiers du dépôt.

Le CORS n'autorise que `https://oufoke.github.io`. Pour un test en local, ajouter
temporairement `http://localhost:1313` dans `ALLOWED_ORIGINS`, puis le retirer.

---

## Déploiement

Hébergé sur Render, tier gratuit. Le service est mis en veille après 15 minutes
sans trafic et redémarre en une minute environ à la requête suivante — le widget
affiche un indicateur d'attente pour couvrir ce cas.

```
Build Command : pip install -r requirements.txt
Start Command : uvicorn app:app --host 0.0.0.0 --port $PORT
```
