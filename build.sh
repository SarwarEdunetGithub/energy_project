#!/usr/bin/env bash
set -euo pipefail

# ensure deps (Vercel auto-installs requirements but running pip here is harmless)
pip install -r requirements.txt

# collect static files into STATIC_ROOT
python manage.py collectstatic --no-input

# apply migrations if you have a DB (you must set DATABASE_URL in Vercel env)
python manage.py migrate --no-input || true
