from app import create_app


def test_config():
    assert not create_app().testing


def test_ping(client):
    resp = client.get('/api/ping')

    assert resp.status_code == 200
    assert resp.json.get('status') == 'ok'
    assert resp.json.get('message') == 'pong!'
