from fastapi.testclient import TestClient
import pytest
from requests.sessions import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.models import Base
from app.main import app
from app import schemas, models
from app.config import settings
from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.DATABASE_USERNAME}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}_test'

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/fastapi_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def overide_get_db():
#     db = TestingSessionLocal()

#     try:
#         yield db
#     finally:
#         db.close() 

# app.dependency_overrides[get_db] = overide_get_db


# client = TestClient(app)
 
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close() 


@pytest.fixture()
def client(session):

    def overide_get_db():

        try:
            yield session
        finally:
            session.close()
    
    app.dependency_overrides[get_db] = overide_get_db

    # run our code before we run our test
    
    yield TestClient(app)

    # run code before test finishes

@pytest.fixture
def test_user2(client):
    user_data = {"email":"hello123@gmail.com", "password":"password123"}

    res = client.post("/users/", json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']
    
    return new_user



@pytest.fixture
def test_user(client):
    user_data = {"email":"hello@gmail.com", "password":"password123"}

    res = client.post("/users/", json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']
    
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id":test_user['id']})


@pytest.fixture
def authorized_client(client, token):

    client.headers = {
        **client.headers,
        "Authorization":f'Bearer {token}'
    }

    return client

@pytest.fixture
def test_posts(test_user, session,test_user2):
    posts_data = [
        {
            "title":"first title",
            "content":"first content",
            "owner_id":test_user['id']
        },
        {
            "title":"second title",
            "content":"second content",
            "owner_id":test_user['id']
        },
        {
            "title":"third title",
            "content":"third content",
            "owner_id":test_user['id']
        },
        {
            "title":"third title",
            "content":"third content",
            "owner_id":test_user2['id']
        }
    ]

    def create_post_model(post):
        return models.Post(**post)

    posts_map = map(create_post_model, posts_data)
    posts = list(posts_map)

    session.add_all(posts)
    session.commit()
    return session.query(models.Post).all()
