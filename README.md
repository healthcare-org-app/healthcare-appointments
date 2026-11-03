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

## Tests

```bash
pytest
```
