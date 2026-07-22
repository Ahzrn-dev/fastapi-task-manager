# 🚀 Task Manager API

A production-style RESTful Task Management API built with **FastAPI**, **SQLAlchemy**, and **SQLite** following a layered architecture.

## ✨ Features

- ✅ Create a new task
- ✅ Retrieve all tasks
- ✅ Retrieve a task by ID
- ✅ Update an existing task
- ✅ Delete a task
- ✅ Interactive API documentation with Swagger UI

---

## 🛠 Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## 📁 Project Structure

```text
app/
├── api/           # API routes
├── core/          # Database configuration
├── models/        # SQLAlchemy models
├── schemas/       # Pydantic schemas
├── services/      # Business logic
└── main.py
```

---

## ⚡ Quick Start

### Clone the repository

```bash
git clone https://github.com/Ahzrn-dev/fastapi-task-manager.git
cd fastapi-task-manager
```

### Create a virtual environment

```bash
python -m venv .venv
```

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive documentation for all endpoints.

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks/` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a task by ID |
| POST | `/tasks/` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## 🚀 Future Improvements

- JWT Authentication
- Docker support
- Unit testing with Pytest
- Alembic database migrations
- Pagination
- Search & filtering
- PostgreSQL support

---

## 👨‍💻 Author

**Amirhossein Zarean**

GitHub:
https://github.com/Ahzrn-dev
