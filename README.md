# Task Management REST API
Django REST Framework + PostgreSQL task workflow API with JWT authentication, owner/staff permissions, filtering, pagination, OpenAPI docs, and pytest coverage.

## Features
- User registration and JWT access/refresh tokens.
- Task CRUD with title, description, status, priority, and due date.
- Users can access their own tasks; staff can access all tasks.
- Filtering by status/priority, search, ordering, and pagination.
- Server-controlled ownership and serializer validation.
- Swagger UI at /api/docs/ and schema at /api/schema/.

## Setup
Use Python 3.11+ and PostgreSQL 14+. Create a database, copy .env.example to .env, and update DATABASE_URL.
1. Create and activate a virtual environment: python -m venv .venv
2. Install: pip install -r requirements.txt
3. Migrate: python manage.py migrate
4. Create admin: python manage.py createsuperuser
5. Run: python manage.py runserver

## API
- POST /api/auth/register/ — create an account.
- POST /api/auth/token/ — obtain JWT tokens.
- POST /api/auth/token/refresh/ — refresh access token.
- GET/POST /api/tasks/ — list/create own tasks.
- GET/PATCH/DELETE /api/tasks/{id}/ — retrieve/update/delete.
Protected routes require Authorization: Bearer ACCESS_TOKEN.

Example registration JSON: {"username":"alex","email":"alex@example.com","password":"StrongPass123!"}

## Tests
Run pytest. Tests use SQLite by default; configure DATABASE_URL for PostgreSQL.

## Structure
- config/: settings, root URLs, WSGI.
- tasks/: model, serializers, permissions, viewsets.
- tests/: registration, ownership, and validation tests.
- .env.example, requirements.txt, pytest.ini, manage.py.

## Design
Ownership is assigned from the authenticated request, never trusted from client input. Object permissions prevent cross-user access. PostgreSQL is selected with DATABASE_URL; SQLite is a convenient fallback for tests and local exploration. Production deployments should use managed secrets, HTTPS, backups, rate limits, and structured logging.


## Folder tree
task-management-rest-api/
|-- config/                 Django project settings and root routes
|-- tasks/                  Task model, serializers, permissions, API views
|-- tasks/migrations/       Database schema migrations
|-- tests/                  Registration, authorization, and validation tests
|-- .github/workflows/      Continuous integration
|-- .env.example            Local configuration template
|-- manage.py               Django command-line entry point
|-- pytest.ini              pytest configuration
|-- requirements.txt        Python dependencies
|-- README.md               Project and API documentation
