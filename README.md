# Portfolio Website (Django)

Personal portfolio website built with Django, including deployment scripts and static/media assets.

## Overview
This repository contains a Django-based portfolio site with custom app views, project data, and production-ready run scripts.

## Repository Structure
- `manage.py`: Django project entry point.
- `personalweb/`: Project configuration (`settings.py`, `urls.py`, ASGI/WSGI).
- `home/`: Application module (views, models, admin, tests).
- `requirements.txt`: Python dependencies.
- `Procfile`, `start.sh`, `build.sh`: Deployment/startup scripts.
- `media/`: Portfolio image/media assets.
- `data.json`: Seed/content data.

## Features
- Portfolio presentation pages
- Django admin integration
- Structured project/app layout for deployment

## Local Setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Run migrations:
   - `python manage.py migrate`
5. Start development server:
   - `python manage.py runserver`

## Deployment Notes
- `Procfile` and shell scripts are included for platform deployment.
- Configure `DEBUG`, `ALLOWED_HOSTS`, and database settings for production.
- For PostgreSQL deployments (Render/Vercel), set `DATABASE_URL` in the form:
  - `postgresql://USER:PASSWORD@HOST:5432/DB_NAME`
- Optional host/origin overrides:
  - `ALLOWED_HOSTS=yourdomain.com,.onrender.com,.vercel.app`
  - `CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://*.onrender.com,https://*.vercel.app`

## Next Improvements
- Add environment variable template (`.env.example`)
- Add test coverage for views/models
- Add screenshots and live demo link
