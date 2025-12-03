 HEAD
# Lune API – Base Project Initialization

This project contains the initial scaffold for the Lune API service.

## Development

Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate

# Lune API

Base structure for the Lune API project.

## Project Structure

```text
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


uvicorn main:app --reload

Installed Core Dependencies

FastAPI

Uvicorn

python-dotenv

Status

Project scaffold initialized and development server running successfully.
 786ad58 (CAS5: Update README with project structure and development info)
