#!/bin/sh
set -e

DB_PATH="${DB_PATH:-/app/data/db.sqlite3}"
SEED_DB="/app/db.sqlite3"
export DB_PATH

mkdir -p "$(dirname "$DB_PATH")"

# Primer arranque con volumen vacio: sembrar con la base incluida en la imagen.
# Nunca sobrescribe una base existente.
if [ ! -f "$DB_PATH" ] && [ -f "$SEED_DB" ]; then
    echo "Volumen sin base de datos: copiando semilla a $DB_PATH"
    cp "$SEED_DB" "$DB_PATH"
fi

python manage.py migrate --noinput

exec gunicorn core.wsgi:application -c gunicorn_config.py
