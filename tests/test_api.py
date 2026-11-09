from app.routes import RESOURCE


def test_crud(client, svc):
    r = client.post(f"/api/{RESOURCE}/", json={"name": "test"})
    assert r.status_code == 201, r.data
    rid = r.get_json()["id"]

    r = client.get(f"/api/{RESOURCE}/{rid}")
    assert r.status_code == 200

    r = client.patch(f"/api/{RESOURCE}/{rid}", json={"name": "updated"})
    assert r.status_code == 200
    assert r.get_json()["name"] == "updated"

    r = client.delete(f"/api/{RESOURCE}/{rid}")
    assert r.status_code == 200

    r = client.get(f"/api/{RESOURCE}/")
    body = r.get_json()
    assert body["count"] >= 1


def test_get_missing(client):
    r = client.get(f"/api/{RESOURCE}/999999")
    assert r.status_code == 404


def test_audit_emitted_on_create(client, svc):
    client.post(f"/api/{RESOURCE}/", json={"name": "audit-me"})
    topics = [t for t, _, _ in svc.bus.published]
    assert "audit.event" in topics


def test_duration_minutes_derived(client):
    r = client.post(f"/api/{RESOURCE}/", json={
        "starts_at": "2026-08-20T14:30:00+00:00",
        "ends_at": "2026-08-20T15:00:00+00:00",
    })
    assert r.status_code == 201, r.data
    assert r.get_json()["duration_minutes"] == 30


def test_duration_minutes_absent_without_end(client):
    r = client.post(f"/api/{RESOURCE}/", json={"starts_at": "2026-08-20T14:30:00+00:00"})
    assert r.status_code == 201, r.data
    assert "duration_minutes" not in r.get_json()
