#!/usr/bin/env bash
set -euo pipefail

echo ">>> Running startup script"

# Apply DB migrations
echo ">>> Applying migrations"
python manage.py migrate --noinput

# Collect static files
echo ">>> Collecting static files"
python manage.py collectstatic --no-input || true

# Create superuser from env vars if provided and not exists
echo ">>> Ensuring superuser exists (if env vars provided)"
python - <<'PY'
import os
from django.contrib.auth import get_user_model
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'denni_ba_proj.settings')
django.setup()
User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
if username and password:
    if not User.objects.filter(username=username).exists():
        print("Creating superuser:", username)
        User.objects.create_superuser(username=username, email=email or '', password=password)
    else:
        print("Superuser already exists:", username)
else:
    print("Superuser env vars not provided; skipping creation")
PY

# Load sample data (non-fatal)
if [ -f "./sample_data.py" ]; then
  echo ">>> Loading sample data (sample_data.py)"
  python sample_data.py || true
else
  echo ">>> No sample_data.py found, skipping"
fi

# Start the server (Render provides $PORT)
echo ">>> Starting gunicorn"
exec gunicorn denni_ba_proj.wsgi --bind 0.0.0.0:${PORT:-10000} --workers 2
