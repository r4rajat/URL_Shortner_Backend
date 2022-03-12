from fastapi.testclient import TestClient
from config import app
import constant


client = TestClient(app)


def test_create_new_short_url_with_preferred_short_url():
    response = client.post(
        '/create-shortened-url',
        json={
            constant.LONG_URL: "www.testing.com",
            constant.PREFERRED_SHORT_URL: "tstng"
        }
    )
    assert response.status_code == 201


def test_create_new_short_url_without_preferred_short_url():
    response = client.post(
        '/create-shortened-url',
        json={
            constant.LONG_URL: "www.testing-2.com"
        }
    )
    assert response.status_code == 201


def test_create_new_short_url_with_preferred_short_url_exist():
    response = client.post(
        '/create-shortened-url',
        json={
            constant.LONG_URL: "www.testing-3.com",
            constant.PREFERRED_SHORT_URL: "tstng"
        }
    )
    assert response.status_code == 201


def test_create_short_url_when_short_url_already_exist():
    response = client.post(
        '/create-shortened-url',
        json={
            constant.LONG_URL: "www.testing-3.com",
            constant.PREFERRED_SHORT_URL: "tstng"
        }
    )
    assert response.status_code == 409


def test_get_short_url_of_existing_long_url():
    response = client.get('/get-shortened-url?long_url=www.testing.com')
    assert response.status_code == 200


def test_get_short_url_of_non_existing_long_url():
    response = client.get('/get-shortened-url?long_url=www.testing-not.com')
    assert response.status_code == 404
