# FAQ — réponses de référence

> Ce fichier est la source prioritaire du chatbot. Il est rédigé par Oumar
> et prime sur toute autre source en cas d'ambiguïté.
>
> Règle de rédaction : les chiffres sont donnés tels qu'ils ont été mesurés.
> Aucun arrondi, aucune reformulation valorisante. Quand un chiffre porte sur
> des données de test ou synthétiques, c'est dit dans la même phrase.

---

## Positionnement

**Que fait Oumar exactement ?**
Data Product Manager. Il pilote des produits data de bout en bout : du cadrage
du besoin métier jusqu'à l'adoption réelle par les utilisateurs. Sa conviction :
« une donnée bien gouvernée qui ne fait pas mieux décider reste de la dette
documentaire bien rangée. »

**Quelle est sa spécialité ?**
Deux axes complémentaires. La gouvernance et la qualité de données — conception
de dispositifs de contrôle conditionnant la publication d'indicateurs. Et l'IA
appliquée — NLP, RAG, systèmes conçus sous contrainte de confidentialité.

**Combien d'années d'expérience ?**
Six ans, chez France Travail au siège, depuis 2020.

**Quel type de poste cherche-t-il ?**
Des postes autour de la gouvernance des données : Data Product Manager, Product
Owner technique sur des sujets data et IA, chef de projet data/IA. En grand
groupe, en cabinet de conseil ou en scale-up structurée.

---

## Parcours

**Quel est son parcours en une phrase ?**
Il est remonté de la production de la donnée vers la décision : d'abord produire
les flux (ETL, SQL, SAS sur IBM Netezza), puis les fiabiliser (contrôles qualité
automatisés), puis les rendre compréhensibles (référentiel documentaire), et
aujourd'hui piloter ce qui les rend utiles (audit d'usage, cockpit décisionnel).

**Quels ont été ses quatre périmètres successifs ?**
Production Big Data d'abord : conception de programmes d'extraction complexes
industrialisés par la DSI, sur des bases nationales à grande échelle. Puis MOA
data : traduction des besoins métier en spécifications et arbitrages techniques,
de la spécification jusqu'à la recette en production. Puis indicateurs nationaux :
pilotage du cycle de vie des indicateurs du marché du travail diffusés
publiquement, en coordination avec les partenaires institutionnels. Enfin
pilotage immobilier : audit d'usage et refonte d'un dispositif de reporting
national.

**Pourquoi cherche-t-il à changer de poste ?**
Le périmètre qu'il porte — cadrage, pilotage produit, livraison de bout en bout —
dépasse le cadre dans lequel il peut le faire évoluer là où il est. Il cherche un
environnement où ce niveau de responsabilité est la norme, sur des contextes plus
variés, avec la data et l'IA comme axe stratégique.

**A-t-il travaillé ailleurs qu'à France Travail ?**
Non. Six ans dans la même organisation, mais sur quatre périmètres successifs très
différents : production Big Data, MOA data, indicateurs nationaux, puis pilotage
immobilier.

**Avec quels interlocuteurs travaille-t-il ?**
Il se situe à l'interface entre la DSI, les directions métier et la direction
générale. Sur son dernier périmètre, ses utilisateurs finaux étaient une direction
nationale et vingt directions régionales. Il a également coordonné des partenaires
institutionnels externes — INSEE, DARES, URSSAF, ministère du Travail — sur la
production d'indicateurs publics.

---

## Réalisations

**Quelle est sa réalisation la plus significative ?**
L'audit d'usage d'un dispositif de reporting immobilier national. Avant de
reconstruire quoi que ce soit, il a mesuré l'usage réel : sur 63 pages
disponibles, 23 concentraient 90 % du trafic, et 19 pages avaient moins de cinq
consultations sur quatre mois. Cette mesure a orienté toute la refonte —
101 indicateurs redéfinis avec la direction, sur un parc de plus de 1 000 sites.

**En quoi consiste ce dispositif de pilotage immobilier ?**
Un tableau de bord décisionnel structuré sur quatre dimensions — surfaces, budget,
schéma directeur, loyers — avec un module comparant les projections aux données
réalisées, une cartographie interactive et un cockpit d'arbitrage. Il est conçu
pour être utilisable sans prérequis technique par des décideurs.

**Qu'a-t-il fait sur l'automatisation de la production ?**
Le cycle de production mensuel reposait sur trois jours de traitement largement
manuel. Il a supprimé l'étape de recopie manuelle par une solution transitoire, et
rédigé l'expression de besoin adressée à la DSI pour l'automatisation complète du
pipeline — quinze exigences fonctionnelles et un plan de migration en cinq phases.
L'automatisation cible relève de la DSI et n'était pas en production à son départ
du périmètre : la distinction entre ce qui est livré et ce qui est spécifié est
maintenue.

**Qu'a-t-il fait en gouvernance data ?**
Il a conçu et déployé un dispositif de contrôles qualité automatisés
conditionnant la publication d'indicateurs publics nationaux : aucune diffusion
sans validation préalable. Et un référentiel documentaire en Docs-as-Code
devenu source unique de vérité pour les règles de gestion, dont l'usage a dépassé
le périmètre initialement visé.

**Comment fonctionne ce dispositif de contrôle qualité ?**
Des tests automatisés portant sur l'intégrité, la fraîcheur et la cohérence
métier des indicateurs, exécutés avant chaque livraison. Le résultat est restitué
dans un tableau de bord de validation qui donne une décision binaire aux équipes
statistiques avant transmission à la DSI. L'objectif produit n'était pas de
détecter plus d'anomalies, mais de rendre impossible une publication non validée.

**Et le référentiel documentaire ?**
Un portail construit en Docs-as-Code, déployé en environnement DSI sécurisé sous
fortes contraintes réseau. Il centralise les règles de gestion, les dictionnaires
de données et les spécifications, traduites depuis SQL et SAS vers une forme
lisible par les équipes de maîtrise d'ouvrage. Il sert de référence au paramétrage
des contrôles qualité. Son intérêt principal est de faire survivre la
connaissance métier au turnover et au départ des prestataires.

**Combien de produits a-t-il livrés ?**
Six produits livrés, dont deux applications publiques.

---

## Projets IA

**Quels projets IA a-t-il construits ?**
Juris Sensus AI, un moteur d'analyse sémantique NLP Zero-Shot. Un assistant RAG
de pré-tri de CV. Un moteur de scoring prédictif explicable. Et un outil de
prévision budgétaire par séries temporelles.

**Qu'est-ce que Juris Sensus AI ?**
Une plateforme d'investigation documentaire destinée aux directions juridiques,
audit et RH. Elle ingère des archives de correspondance et les passe au crible de
plusieurs moteurs d'analyse : détection de fraude par croisement avec des bases
structurées, analyse des communications hostiles, repérage de contradictions
factuelles ou temporelles. Le pipeline repose sur de la classification Zero-Shot
(mDeBERTa-v3), avec une interface de navigation dans les résultats et une
génération de rapports.

**Quels sont les chiffres mesurés sur Juris Sensus ?**
3 609 documents traités en moins de quatre heures, environ 650 documents
critiques extraits et catégorisés, le tout en exécution sur une machine
contrainte (16 Go de RAM). Ces chiffres proviennent d'un corpus de test
représentatif, mesurés et non simulés.

**Pourquoi une exécution 100 % locale ?**
C'était une contrainte de départ, pas une optimisation. Les corpus visés
contiennent des données sensibles : les externaliser vers des LLM publics
exposerait à des violations du RGPD et à la perte du secret des affaires.
L'architecture a donc été conçue sans aucun appel API externe. C'est une
décision produit assumée, avec son coût : pas d'accès aux modèles propriétaires
les plus performants.

**Sur quoi travaille-t-il actuellement en IA ?**
Une version 2 de Juris Sensus en architecture multi-agents, pour passer d'un
pipeline d'analyse à un système décisionnel. Et un framework multi-agents d'audit
qualité data articulant audit, restitution et alerte. Les deux sont en cours, pas
terminés.

**Qu'est-ce que l'assistant de pré-tri de CV ?**
Une application analysant la compatibilité entre un CV et une offre d'emploi :
extraction du texte, évaluation sur critères sémantiques plutôt que par mots-clés,
synthèse des points forts et points de vigilance, et génération de questions
d'entretien ciblées sur les zones à creuser. Architecture RAG simplifiée
(LangChain, GPT-4o), déployée publiquement sur Streamlit.

**Qu'est-ce que le moteur de lead scoring ?**
Un moteur de scoring prédictif qui priorise des prospects B2B par probabilité de
conversion, avec explication du score par variable via SHAP — le choix de
l'explicabilité visait l'adoption par des équipes commerciales, qui n'utilisent
pas un score qu'elles ne comprennent pas. Modèle XGBoost entraîné sur un jeu de
données synthétique de 2 000 prospects. Performance mesurée sur ce jeu : 89 % de
justesse globale, 79 % de précision sur la classe positive.

**Et l'outil de prévision budgétaire ?**
Un outil de forecasting financier décomposant les flux en tendance et
saisonnalités (Prophet), pour anticiper les tensions de trésorerie à 30, 60 et
90 jours. Les données utilisées sont simulées.

---

## Compétences et limites

**Quelle est sa stack technique ?**
Solide : SQL avancé (fenêtrage, CTE, jointures complexes), SAS, Python, R,
IBM Netezza, IBM Cloud Pak for Data, Power BI et DAX, Digdash, Streamlit,
Git et GitLab CI/CD. Côté IA : NLP Zero-Shot (HuggingFace), RAG (LangChain,
OpenAI). Il a également travaillé sur des données issues de SAP RE-FX.

**Comment travaille-t-il, méthodologiquement ?**
Il mesure avant de reconstruire : sur son dernier périmètre, l'audit quantitatif
d'usage a précédé toute décision de refonte. Il définit les métriques de succès
avant la livraison plutôt qu'après. Et il documente pour la passation, l'objectif
étant qu'un produit tienne sans lui.

**Connaît-il Snowflake, BigQuery, dbt, Airflow ?**
Non pour Snowflake, BigQuery et Airflow — il ne les a pas pratiqués. Sur dbt,
il a eu un premier contact en certification, sans expérience projet. Il a en
revanche déjà mené plusieurs bascules d'outillage : SQL vers SAS, BI classique
vers Power BI, ML classique vers NLP appliqué.

**A-t-il de l'expérience en ESN ou avec des clients externes ?**
Non. Ses six ans sont en interne. Il a eu des clients internes exigeants —
20 directions régionales, des arbitrages à défendre devant des directeurs, et
aucun droit à l'erreur sur des données publiées nationalement. Mais il n'a pas
connu la pression contractuelle d'une mission facturée.

**Ses projets IA ont-ils été déployés chez des clients ?**
Non. Les applications Streamlit sont publiques et testées par de vrais
utilisateurs, mais sur données synthétiques et sans contrat client. Juris Sensus
a tourné sur un corpus réel dans un contexte interne : les chiffres annoncés sont
mesurés, pas simulés.

**A-t-il managé une équipe ?**
Pas de management hiérarchique documenté. Ce qui est documenté relève du
leadership transverse : alignement de plusieurs directions sur des produits menés
en parallèle, et acculturation d'une dizaine de chargés de maîtrise d'ouvrage aux
méthodes agiles.

**Quelles sont les limites de son profil ?**
Trois, qu'il énonce lui-même sans détour. Pas de client externe payant : six ans
en interne. Pas de certification spécialisée en gouvernance de type DAMA ou DCAM :
sa gouvernance s'est apprise en conditions réelles. Et des projets de portfolio
qui sont de vrais produits déployés, mais non contractualisés avec des clients
payants.

---

## Formation

**Quelle est sa formation ?**
Master 2 Ingénierie Statistique et Data Science (ISIFAR), Université Paris Cité,
2018. Master 1 Mathématiques, Modélisation, Apprentissage, Université Paris Cité.
Cycle ingénieur Mathématiques Appliquées à Sup Galilée, niveau L3. Classes
préparatoires PCSI/PC.

**Est-il ingénieur ?**
Il a suivi un cycle ingénieur en mathématiques appliquées à Sup Galilée jusqu'au
niveau L3, sans obtenir le titre d'ingénieur. Son diplôme le plus élevé est le
Master 2 ISIFAR.

**Quelles certifications a-t-il ?**
Data Product Manager (DataScientest, certifiée Sorbonne), AI Engineer for Data
Scientists Associate (DataCamp), Data Scientist Professional (DataCamp),
Data Engineer Associate, plus des certifications en gouvernance (RGPD, AI Act)
et data quality.

**Quel est son niveau d'anglais ?**
Courant, lu écrit et parlé. Son portfolio est disponible en français et en anglais.

---

## Sujets à ne pas traiter

Le chatbot ne répond pas aux questions portant sur :

- la rémunération, les prétentions salariales ou le salaire actuel
- la date de disponibilité précise ou les modalités de préavis
- l'employeur actuel au-delà de ce qui est publiquement documenté
- les autres candidatures ou processus de recrutement en cours
- la vie personnelle

Réponse type dans ces cas : « Ce sujet se traite directement avec Oumar. Vous
pouvez le contacter à oumarfodek@gmail.com ou via LinkedIn. »

---

## Contact

Email : oumarfodek@gmail.com
LinkedIn : linkedin.com/in/oumarfodek
GitHub : github.com/oufoke
Portfolio : oufoke.github.io
