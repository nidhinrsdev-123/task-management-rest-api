# Task Management REST API

A JWT-authenticated task management backend built with **Python, Django REST Framework, PostgreSQL, and Pytest**. It demonstrates REST API design, relational models, ownership-based permissions, filtering, pagination, and automated tests.

## Features
- User registration and JWT access/refresh tokens.
- Task CRUD with title, description, status, priority, and due date.
- Users can access their own tasks; staff users can access all tasks.
- Filter by status/priority, search, ordering, and pagination.
- Server-assigned ownership, validation, and OpenAPI/Swagger documentation.

## Technology
Python 3.11+, Django 5, Django REST Framework, Simple JWT, django-filter, drf-spectacular, PostgreSQL (SQLite fallback), and pytest.

## Exact repository structure

This tree matches the files currently committed to GitHub:

~~~text
task-management-rest-api/
├── .github/
│   └── workflows/
│       └── tests.yml
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   └── views.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── .env.example
├── .gitignore
├── LICENSE
├── manage.py
├── pytest.ini
├── README.md
└── requirements.txt
~~~

## Step-by-step: run locally (Windows)

### 1. Install prerequisites
Install Python 3.11 or newer. PostgreSQL 14+ is optional for the quick start; the app uses SQLite automatically if DATABASE_URL is not set.

Check Python:

~~~powershell
py --version
~~~

### 2. Clone the repository

~~~powershell
git clone https://github.com/nidhinrsdev-123/task-management-rest-api.git
cd task-management-rest-api
~~~

### 3. Create and activate a virtual environment

~~~powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
~~~

If PowerShell blocks activation, use Command Prompt:

~~~bat
.venv\Scripts\activate.bat
~~~

### 4. Install dependencies

~~~powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
~~~

### 5. Configure the database

**Quick start with SQLite:** Skip this step. The project creates db.sqlite3 when migrations run.

**Use PostgreSQL:** Create a PostgreSQL database and user. Copy the example environment file:

~~~powershell
Copy-Item .env.example .env
~~~

Edit DATABASE_URL in .env using your own credentials. Example format:

~~~text
DATABASE_URL=postgresql://task_user:your_password@localhost:5432/task_manager
~~~

Do not commit .env or real credentials to GitHub.

### 6. Create database tables

~~~powershell
python manage.py migrate
~~~

### 7. Create an administrator account

~~~powershell
python manage.py createsuperuser
~~~

Follow the prompts.

### 8. Start the development server

~~~powershell
python manage.py runserver
~~~

Open:
- API: http://127.0.0.1:8000/api/
- Swagger docs: http://127.0.0.1:8000/api/docs/
- OpenAPI schema: http://127.0.0.1:8000/api/schema/
- Django admin: http://127.0.0.1:8000/admin/

Stop the server with Ctrl+C.

## API endpoints

Base URL: http://127.0.0.1:8000

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/auth/register/ | Register a user |
| POST | /api/auth/token/ | Obtain JWT tokens |
| POST | /api/auth/token/refresh/ | Refresh access token |
| GET, POST | /api/tasks/ | List or create tasks |
| GET, PATCH, DELETE | /api/tasks/{id}/ | Retrieve, update, delete |

### 1. Register a user

POST /api/auth/register/ JSON body:

~~~json
{
  "username": "alex",
  "email": "alex@example.com",
  "password": "StrongPass123!"
}
~~~

### 2. Obtain a JWT token

POST /api/auth/token/ JSON body:

~~~json
{
  "username": "alex",
  "password": "StrongPass123!"
}
~~~

Copy the returned access token. Protected requests require this header:

~~~text
Authorization: Bearer YOUR_ACCESS_TOKEN
~~~

### 3. Create a task

POST /api/tasks/ with the bearer token:

~~~json
{
  "title": "Learn Django REST Framework",
  "description": "Build and test my first API",
  "status": "todo",
  "priority": "high"
}
~~~

The server assigns the owner from the authenticated account.

### 4. List and filter tasks
- /api/tasks/
- /api/tasks/?status=todo
- /api/tasks/?priority=high
- /api/tasks/?search=django
- /api/tasks/?ordering=created_at
- /api/tasks/?page=2

## Run tests

From the repository root:

~~~powershell
pytest
~~~

Tests cover registration, task creation, user ownership isolation, and invalid status validation. SQLite is used by default; set DATABASE_URL to run against PostgreSQL.

## Code explanation
- config/settings.py: installed apps, database, JWT authentication, pagination, and schema configuration.
- config/urls.py: authentication, task, and documentation routes.
- tasks/models.py: Task database model and status/priority choices.
- tasks/serializers.py: input validation and JSON representation.
- tasks/permissions.py: owner-or-staff access rule.
- tasks/views.py: registration endpoint and task CRUD viewset.
- tasks/migrations/: database schema history.
- tests/: automated API behavior tests.

## Security notes
The default secret key is for local development only. Before deployment, set a strong SECRET_KEY, DEBUG=False, configure ALLOWED_HOSTS, use HTTPS, and keep credentials out of Git.
