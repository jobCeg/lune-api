# Lune API – Base Project Initialization

This project contains the initial scaffold for the Lune API service.

## Development

Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate

Run the development server:

uvicorn main:app --reload

Base Structure for the Lune API Project

lune-api/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── service.py
│   ├── core/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   └── services/
│       └── __init__.py
├── main.py
├── README.md
└── venv/

nstalled Core Dependencies

FastAPI

Uvicorn

python-dotenv

Database Migrations

Install Alembic and python-dotenv:

pip install alembic python-dotenv

Create migrations (empty initially or with models when available):

alembic revision -m "migration message"

Apply migrations to the database:

alembic upgrade head

Status

Project scaffold initialized 

Development server running successfully 

Database migration tool (Alembic) configured

## API Endpoint
https://lune-api-production.up.railway.app/
