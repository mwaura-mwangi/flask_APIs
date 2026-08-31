# Flask & Jinja2 Todo App

A lightweight, full-stack Web Application and RESTful API built with **Flask**, **Flask-SQLAlchemy**, and **Jinja2** template rendering. Managed using **`uv`** for fast Python dependency and virtual environment administration.

---

## Project Architecture

This project provides both an interactive server-side rendered UI and a REST API backend sharing a common database layer.

```text
to_do_list/
├── app/
│   ├── templates/
│   │   └── index.html      # Jinja2 template for the web frontend
│   ├── __init__.py         # Application factory & DB setup
│   ├── models.py           # SQLAlchemy database models
│   └── routes.py           # REST API blueprint routes (/api/todos)
├── config.py               # Application configuration settings
├── run.py                  # Main entry point serving UI & API routes
├── pyproject.toml          # Project metadata & dependencies
└── README.md               # Project documentation
```

---

## Features

- **Jinja2 Frontend**: Simple, clean interface for creating, viewing, and deleting tasks without requiring frontend build tools or external JavaScript frameworks.
- **RESTful API**: Clean blueprint routes operating under `/api/todos/` supporting `GET`, `POST`, `PUT`, and `DELETE` requests.
- **ORM Integration**: Powered by **Flask-SQLAlchemy** with structured data models and quick record querying/modifications (`db.get_or_404`).
- **Modern Package Management**: Managed seamlessly using **`uv`**.

---

## Quick Start

### 1. Prerequisites
Ensure you have **Python 3.10+** and **`uv`** installed.

### 2. Installation & Setup
Clone the repository and install dependencies using `uv`:

```bash
# Clone the repository
git clone <your-repository-url>
cd to_do_list

# Sync and install dependencies into a virtual environment
uv sync
```

### 3. Running the Server
Launch the Flask development server:

```bash
uv run python run.py
```

The server will start at `http://127.0.0.1:5000/`.

---

## Application Usage

### Web Interface (Jinja2)
Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```
From here, you can add new tasks directly via the input form or delete completed items.

---

## REST API Endpoints

The application exposes a standard JSON API prefixed with `/api/todos`:

| Method | Endpoint | Description | Request Body | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/todos/` | Fetch all todo items | None | `[ { "id": 1, "title": "Task", "completed": false } ]` |
| `GET` | `/api/todos/<id>` | Fetch a single todo item by ID | None | `{ "id": 1, "title": "Task", "completed": false }` |
| `POST` | `/api/todos/` | Create a new todo item | `{ "title": "New Task", "completed": false }` | `{ "id": 2, "title": "New Task", "completed": false }` |
| `PUT` | `/api/todos/<id>` | Update an existing todo item | `{ "title": "Updated", "completed": true }` | `{ "id": 1, "title": "Updated", "completed": true }` |
| `DELETE` | `/api/todos/<id>` | Delete a todo item by ID | None | `{ "message": "Todo deleted successfully" }` |

### API Quick Test (cURL)

**Create a Todo:**
```bash
curl -X POST http://127.0.0.1:5000/api/todos/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Build Flask Application", "completed": false}'
```

**Get All Todos:**
```bash
curl http://127.0.0.1:5000/api/todos/
```

---

## Environment & Dependencies

- **Python**: `^3.10`
- **Flask**: Application framework
- **Flask-SQLAlchemy**: Object-Relational Mapping (ORM)
- **Flask-Migrate**: Database schema migrations
- **uv**: Environment and package manager