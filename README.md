# Task Manager API

A RESTful Task Management API built with FastAPI, SQLAlchemy, and SQLite.

## Features

- Create tasks
- Get all tasks
- Get a task by ID
- Update tasks
- Delete tasks
- Interactive API documentation with Swagger

## Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```
app/
├── api/
├── core/
├── models/
├── schemas/
├── services/
└── main.py
```

## Installation

```bash
git clone <repository-url>
cd fastapi-task-manager

python -m venv .venv

source .venv/bin/activate     # macOS/Linux
# .venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## API Documentation

Open:

```
http://127.0.0.1:8000/docs
```

## Author

Amirhossein Zarean