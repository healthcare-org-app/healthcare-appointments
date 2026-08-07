# appointments-service

appointments-service — domain: appointments

- **Port:** 8600
- **Language:** Python 3.11 + Flask
- **Database:** `appointments` (Postgres, table `appointments`)
- **Event bus:** Kafka

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
pip install -e ../../libs/py-healthcare-common
pip install -r requirements.txt
cp .env.example .env
(cd ../../infra && docker compose up -d postgres kafka kafka-init)
python -m app.main
```

## Tests

```bash
pytest
```
