from app import schemas
from app.oauth2 import ALGORITHM, SECRET_KEY
import pytest
from jose import jwt
from app.config import settings

SECRET_KEY=settings.SECRET_KEY
ALGORITHM=settings.ALGORITHM


def test_create_user(client):
    res = client.post("/users/", json={"email":"hello@gmail.com", "password":"password123"})


    new_user = schemas.UserOut(**res.json())
    assert res.json().get("email") == "hello@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username":test_user["email"], "password":test_user["password"]}
    )

    login_res = schemas.Token(**res.json())

    payload = jwt.decode(login_res.access_token, SECRET_KEY, algorithms=[ALGORITHM])

    id:str = payload.get("user_id")

    assert id == test_user["id"]
    assert login_res.token_type == 'Bearer'

    assert res.status_code == 200 

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('hello@gmail.com', 'wrong_password', 403),
    ('wrongemail@gmail.com', 'wrong_password', 403),
    (None, 'password123', 422),
    ('hello@gmail.com', None, 422),
])
def test_incorrect_login(test_user, client, email, password, status_code):
    response = client.post("/login", data={'username':email, 'password':password})

    assert response.status_code == status_code
    # assert response.json().get('detail') == "Invalid credentials"


