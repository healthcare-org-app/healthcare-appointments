# appointments-service

appointments-service — domain: appointments

- **Port:** 8600
- **Language:** Python 3.11 + Flask
- **Database:** `appointments` (Postgres, table `appointments`)
- **Event bus:** Postgres LISTEN/NOTIFY (via healthcare-common)

## API

| Method    | Path                       |
|-----------|----------------------------|
| GET       | `/api/appointments/`          |
| POST      | `/api/appointments/`          |
| GET       | `/api/appointments/<id>`      |
| PUT/PATCH | `/api/appointments/<id>`      |
| DELETE    | `/api/appointments/<id>`      |
| GET       | `/health`                  |
| GET       | `/ready`                   |

## Events

**Publishes:** appointment.booked, appointment.cancelled
**Subscribes:** (none)

## HTTP peer dependencies

- `patients-service`
- `providers-service`
- `appointment-slots-service`
- `room-booking-service`
- `notifications-service`
- `audit-log-service`

## Local dev

```bash
pip install -r requirements.txt
cp .env.example .env
# Any Postgres works (e.g. the healthcare-infra repo's docker compose); point DATABASE_URL at it
export DATABASE_URL=postgresql://user:pass@localhost:5432/appointments
AUTH_DISABLED=1 python -m app.main   # listens on port 8600
```

Tests use an in-memory FakeDB and need no Postgres: `pip install pytest pytest-mock responses && pytest`.

## Quality gate

Every push and pull request runs the [platform API quality gate](https://github.com/healthcare-org-app/healthcare-api-quality-gate) (`quality-gate` check). It reads `openapi.yaml` and the Postman collection in `postman/collections/Appointments API/` (not the Python code) and rates the contract from A to E, passing at B or better: contract lint (Postman governance), contract tests (the collection run against a mock generated from the spec), coverage of the operations, AI readiness, impact on consumers in the Postman Context Graph (breaking changes block), and the committed Postman skills.

Status: `quality-gate: B or better required` (see the check on each PR for the actual rating).

Run it locally (Node 22+, Postman CLI 1.76.0, `postman login` for the full verdict; no server needed):

```bash
npx github:healthcare-org-app/healthcare-api-quality-gate#v1 run
```

The report lands in `gate-results/`. The collection targets `http://localhost:8600` and never calls a real server.

## Tests

```bash
pytest
```
