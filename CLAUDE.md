# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

PromAdmin is a small Django 5.2 project (UI language `es-mx`, timezone `America/Mexico_City`) that tracks graduation-party ticket payments per student. There is no custom frontend: everything is the Django admin, themed with `django-unfold`. `core/urls.py` only exposes `admin/`; `tickets/views.py` and `tickets/tests.py` are empty stubs.

## Commands

```bash
python manage.py runserver          # dev server (uses .venv; set DEBUG=True in .env for dev)
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput   # output goes to staticfiles/ (committed to git)
python manage.py test tickets       # no tests exist yet
docker compose up --build           # production-like run: entrypoint.sh migrates, then gunicorn on :8000
```

No linter is configured.

## Architecture

- `tickets/models.py`: two models. `Alumno` (student: `nombre`, `invitados_min`/`invitados_max` ticket range, `estado` ∈ pendiente / al_corriente / prorroga) and `Pago` (payment: FK to Alumno, `cantidad_boletos`, `fecha_subida`, `comprobante` image stored on **Cloudinary** via `CloudinaryField`). Payments are counted in tickets, not money (the `monto` field was removed in migration 0004).
- `tickets/admin.py`: all app behavior lives here.
  - `AlumnoAdmin` annotates `total_boletos = Sum('pagos__cantidad_boletos')` in `get_queryset` so the `boletos_pagados` column is sortable. It also makes `estado` inline-editable in the list view (`list_editable` is set per-request in `changelist_view`).
  - Non-superusers get `nombre`, `invitados_min` and `invitados_max` as read-only (`get_readonly_fields`), so staff can only change `estado` and add `Pago` rows.
  - `get_image_html` renders a click-to-zoom receipt thumbnail. It is shared by `PagoInline`, `PagoAdmin` and `AlumnoAdmin.ultimo_comprobante`.
- `core/settings.py`: config comes from `.env` through `python-dotenv`. Required vars are `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, `SECRET_KEY` and `DEBUG` (the string `"True"` enables it). `ALLOWED_HOSTS` is hardcoded in settings (Azure hostname, IP, localhost). The `ALLOWED_HOSTS` entry in `.env` is not read.

## Gotchas

- **SQLite path mismatch:** `settings.py` uses `BASE_DIR / 'db.sqlite3'`, but `docker-compose.yml` mounts the `sqlite_data` volume at `/app/data` and the Dockerfile creates that directory. The container therefore writes to `/app/db.sqlite3` inside the image layer, not the volume, and data is lost on rebuild unless this is reconciled.
- `.gitignore` lists `*.sqlite3`, yet `db.sqlite3` is tracked and used as a backup/transport of production data. Commits like "backup base de datos" are the data-sync mechanism. Treat the file as real data. Ad-hoc `db.sqlite3.bak_*` copies and `conteo_boletos.txt` (ticket-count report) are untracked leftovers from manual data fixes.
- `gunicorn_config.py` binds to `127.0.0.1:8000`, which is unreachable through Docker's published port. This works only behind a reverse proxy on the same host, so a container needs `bind` overridden to `0.0.0.0:8000`.
- `requirements.txt` is UTF-16 encoded. Re-encode it to UTF-8 before editing or diffing it, and keep it pip-readable.
- `settings.py` header comments mention Django 6.0, but the pinned version is 5.2.7.
