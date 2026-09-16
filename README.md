# Assistant portfolio — API

Backend du chatbot de oufoke.github.io. FastAPI + API Claude, sans RAG
(corpus ~45 Ko tenant en contexte, prompt système mis en cache).

| Méthode | Route     | Description                        |
|---------|-----------|------------------------------------|
| GET     | `/health` | Disponibilité                      |
| POST    | `/chat`   | Question → réponse (10 req/min/IP) |

`ANTHROPIC_API_KEY` est défini dans les variables d'environnement Render.
