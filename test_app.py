from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask App!" in response.data

def test_add():
    tester = app.test_client()
    response = tester.get('/add/5/3')
    assert response.status_code == 200
    assert b"8" in response.data
