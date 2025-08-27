# Den Ni Ba — Backend (Django / DRF)

**Den Ni Ba** (\"enfant et maman\" en bambara) — backend API pour recenser lieux sûrs et fournir un forum d'échange vocal pour jeunes femmes à Bamako.

## Objectif
MVP : recensement lieux (centres de santé, pharmacies, associations), micro-forum (posts courts + vocaux), auth JWT. Déploiement cible : 30 août 2025.

## Setup local (rapide)
1. Créer et activer virtualenv:
   `python -m venv .venv && source .venv/bin/activate`
# Si Windows (PowerShell)
`python -m venv .venv && .venv\\Scripts\\Activate.bat`


2. Installer dépendances:
   `pip install -r requirements.txt`
3. Migrer et créer superuser:
   `python manage.py migrate`
   `python manage.py createsuperuser`
4. Lancer serveur:
   `python manage.py runserver`

## Endpoints clés (MVP)
- `POST /api/token/` — obtenir token JWT
- `GET/POST /api/lieux/` — CRUD lieux
- `GET/POST /api/posts/` — timeline, créer post (option audio)
- `POST /api/vocals/` — upload audio

## Documentation & journal
- `EVOLUTION.md` contient le journal d'avancement et messages prêts pour X / ALX eHub.

## Déploiement
Voir `EVOLUTION.md` pour checklist rapide Railay/Render. Contact pour aide au déploiement : [ton nom / contact].
