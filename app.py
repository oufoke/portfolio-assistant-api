"""
API web du chatbot portfolio.

Enveloppe la classe Bot (bot.py, inchangée) dans un endpoint FastAPI,
pour déploiement sur un Hugging Face Space et appel depuis le widget
du site (oufoke.github.io).

Usage local :
    export ANTHROPIC_API_KEY=...   # déjà dans ~/.zshrc normalement
    pip install -r requirements.txt
    uvicorn app:app --reload --port 7860

Test rapide une fois lancé :
    curl -X POST http://localhost:7860/chat \
         -H "Content-Type: application/json" \
         -d '{"question": "Quel est son parcours ?"}'
"""

from typing import Literal, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from bot import Bot

# N'autorise que le site en production. Ajoute http://localhost:1313
# temporairement si tu veux tester le widget contre l'API en local.
ALLOWED_ORIGINS = [
    "https://oufoke.github.io",
    "http://localhost:1313",   # TEMPORAIRE — à retirer avant la mise en ligne
]

MAX_QUESTION_LENGTH = 500
MAX_HISTORY_TURNS = 8  # messages conservés (user+assistant confondus)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Assistant portfolio — Oumar Fodé Kebe")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Chargé une seule fois au démarrage du Space, pas à chaque requête.
bot = Bot()


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=MAX_QUESTION_LENGTH)
    history: Optional[list[ChatMessage]] = None
    lang: Optional[Literal["fr", "en"]] = None


class ChatResponse(BaseModel):
    answer: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
def chat(request: Request, payload: ChatRequest):
    history = [m.model_dump() for m in (payload.history or [])]
    history = history[-MAX_HISTORY_TURNS:]  # borne côté serveur, même si l'appelant envoie plus

    try:
        answer = bot.ask(payload.question, history, lang=payload.lang)
    except Exception:
        raise HTTPException(status_code=502, detail="Erreur du service. Réessayez dans un instant.")

    return ChatResponse(answer=answer)
