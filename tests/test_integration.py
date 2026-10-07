from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Task Manager" in response.data


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/add",
        data={"title": "купить молоко"},
        follow_redirects=True,
    )

    assert response.status_code == 200
