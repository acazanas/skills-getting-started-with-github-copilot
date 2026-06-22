def test_root_redirect(client):
    r = client.get("/", follow_redirects=False)
    assert r.status_code in (307, 302)
    assert r.headers.get("location", "").endswith("/static/index.html")
