# EVOLUTION - Den Ni Ba

Objectif : livrer le MVP Den Ni Ba (recensement lieux + forum vocal) déployé.

---

## Start Phase 1
- Tâches réalisées aujourd'hui :
  - Initialisation du repo local (git), creation virtualenv, création projet Django et app `denniba`.
  - Ajout de .gitignore, requirements.txt, README.md initial.
  - Modèles de base et snippets fournis (User personnalisé, Place).
- Difficultés rencontrées :
  - Perte de temps initiale (deadline serrée). Besoin d’un plan de rattrapage.
- Solutions/contournements :
  - Prioriser le MVP (lieux + posts + upload audio minimal).
- Temps passé :
  - ~3-4 heures/jours
- Prochaines actions :
  - Intégrer modèle forum (Post, Vocal, Comment), config JWT, tests basiques.
  - Configurer settings (AUTH_USER_MODEL, MEDIA_ROOT/URL).
  - Pousser sur GitHub et préparer déploiement sur Railway/Render.
- Status X (tweet court) :
  - "Lancement Den Ni Ba — backend Django pour mamans & enfants à Bamako. #DenNiBa #ALX"
- Status ALX eHub :
  - "Démarrage du backend Den Ni Ba (forum vocal + recensement lieux). Besoin retours sur storage audio en free tier."

---

## Phase 2
- Tâches réalisées aujourd'hui :
  - Intégration modèles forum (Post, Vocal, Comment).
  - Implémentation serializer + viewsets de base.
  - Tests unitaires basiques ajoutés (création post, upload vocal).
- Difficultés rencontrées :
  - Gestion du stockage des fichiers audio sur environnement local / contrainte taille.
- Solutions/contournements :
  - Limiter la taille audio à 2MB et valider côté backend.
  - Documenter options de stockage (Railway volume, Render disk, ou bucket S3).
- Temps passé :
  - Estimé 4-6 heures
- Prochaines actions :
  - Déployer en staging sur Railway/Render, corriger erreurs d’environnement.
  - Préparer sample data (5 lieux, 5 posts vocaux) pour la démo Loom.
- Status X :
  - "Intégration forum & upload audio avancée sur Den Ni Ba. Test de stockage audio en cours. #DenNiBa"
- Status ALX eHub :
  - "Prochaine étape : déploiement sur Railway/Render et tests finaux. Merci pour conseils sur stockage audio."

---

## Last Phase for the Captsone
- Tâches réalisées aujourd'hui :
  - Déploiement sur Railway/Render (staging) + réglage DB PostgreSQL.
  - Tests finaux : endpoints, upload vocal, timeline, filtres lieux.
  - Préparation vidéo demo Loom (script prêt).
- Difficultés rencontrées :
  - Erreurs d’ENV (SECRET_KEY, DEBUG=False, ALLOWED_HOSTS).
- Solutions/contournements :
  - Utiliser `.env` et python-dotenv / variables Railway, vérifier collectstatic et MEDIA settings.
  - Réduire features non critiques pour la démo (pas de RDV ni intégration stock meds).
- Temps passé :
  - Estimé 4-6 heures
- Prochaines actions :
  - Enregistrer la video Loom (2-4 min), poster sur X & ALX eHub, finaliser README & livrables.
- Status X :
  - "Den Ni Ba déployé en staging — demo Loom prévue. #DenNiBa #ALX"
- Status ALX eHub :
  - "Version MVP déployée, merci à tous pour le soutien. Demo Loom et repo dispo — demande retours."

