# Portfolio — Django + DRF + Vue 3 + Vite + Tailwind

A production-ready starter with split settings, JWT auth, Postgres, logging, testing, and a responsive Vue frontend.

## Backend setup

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

## Notes

- JWT endpoints: `/api/auth/token/`, `/api/auth/token/refresh/`
- Current user endpoint: `/api/auth/me/`
- Projects endpoint: `/api/portfolio/projects/`
- Logging to console and `backend/logs/app.log`
- PEP 8 via Black & Ruff; enable with `pre-commit install`
