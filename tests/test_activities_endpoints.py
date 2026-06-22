from fastapi.testclient import TestClient


def test_get_activities(client: TestClient):
    r = client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert "Chess Club" in data


def test_signup_success(client: TestClient):
    email = "newstudent@mergington.edu"
    r = client.post("/activities/Chess%20Club/signup", params={"email": email})
    assert r.status_code == 200
    assert f"Signed up {email} for Chess Club" in r.json().get("message", "")
    assert email in client.get("/activities").json()["Chess Club"]["participants"]


def test_signup_duplicate(client: TestClient):
    email = "michael@mergington.edu"
    r = client.post("/activities/Chess%20Club/signup", params={"email": email})
    assert r.status_code == 400


def test_signup_unknown_activity(client: TestClient):
    r = client.post("/activities/Nonexistent/signup", params={"email": "x@x.com"})
    assert r.status_code == 404


def test_delete_participant_success(client: TestClient):
    email = "temp@student.edu"
    client.post("/activities/Art%20Club/signup", params={"email": email})
    r = client.delete("/activities/Art%20Club/participants", params={"email": email})
    assert r.status_code == 200
    assert email not in client.get("/activities").json()["Art Club"]["participants"]


def test_delete_participant_not_found(client: TestClient):
    r = client.delete("/activities/Art%20Club/participants", params={"email": "noone@x.com"})
    assert r.status_code == 404
