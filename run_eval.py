#!/usr/bin/env python3
"""
Évaluation du chatbot déployé sur Render.

    python3 run_eval.py            # les 22 questions
    python3 run_eval.py piege      # seulement les pièges
"""

import json
import re
import sys
import time
import urllib.request

API = "https://portfolio-assistant-api-ldt7.onrender.com/chat"
DELAY = 7  # rate limit à 10 req/min côté serveur


def detect_lang(question: str) -> str:
    """Un test rédigé en anglais doit être envoyé avec lang=en."""
    marqueurs_en = r"\b(what|which|how|why|who|his|he|does|answer in english|ignore)\b"
    return "en" if re.search(marqueurs_en, question, re.I) else "fr"


def ask(question: str, lang: str) -> str:
    data = json.dumps({"question": question, "lang": lang}).encode()
    req = urllib.request.Request(
        API, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        return json.loads(urllib.request.urlopen(req, timeout=120).read())["answer"]
    except Exception as e:
        return f"[ERREUR] {e}"


def main():
    tests = json.load(open("eval_set.json"))
    filtre = sys.argv[1] if len(sys.argv) > 1 else None
    if filtre:
        tests = [t for t in tests if filtre in t["type"]]

    print(f"Cible : {API}")
    print(f"{len(tests)} questions · ~{len(tests) * DELAY // 60} min\n")

    for i, t in enumerate(tests, 1):
        lang = detect_lang(t["question"])
        reponse = ask(t["question"], lang)

        print("=" * 72)
        print(f"[{i}/{len(tests)}] {t['type'].upper()} · lang={lang}")
        print(f"Q : {t['question']}")
        print(f"Attendu : {t['attendu']}")

        # Signaux à vérifier automatiquement — ne remplace pas la relecture.
        alertes = []
        if "279" in reponse:
            alertes.append("chiffre 279 présent (formulation verrouillée : 23/63)")
        if re.search(r"\bje\b|\bmon\b|\bmes\b", reponse, re.I) and "«" not in reponse:
            alertes.append("première personne possible — à vérifier")
        for montant in re.findall(r"\b\d{2}\s?k\b|\b\d{2}\s?000\s?€", reponse, re.I):
            alertes.append(f"montant cité : {montant}")
        if alertes:
            print("⚠ " + " · ".join(alertes))

        print(f"\nRéponse :\n{reponse}\n")
        if i < len(tests):
            time.sleep(DELAY)


if __name__ == "__main__":
    main()
