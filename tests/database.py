# from fastapi.testclient import TestClient
# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from app.database import get_db
# from app.models import Base
# from app.main import app
# from app import schemas
# from app.config import settings

# SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.DATABASE_USERNAME}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}_test'

# #SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/fastapi_test"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # def overide_get_db():
# #     db = TestingSessionLocal()

# #     try:
# #         yield db
# #     finally:
# #         db.close() 

# # app.dependency_overrides[get_db] = overide_get_db


# # client = TestClient(app)
 
# @pytest.fixture()
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()

#     try:
#         yield db
#     finally:
#         db.close() 


# @pytest.fixture()
# def client(session):

#     def overide_get_db():

#         try:
#             yield session
#         finally:
#             session.close()
    
#     app.dependency_overrides[get_db] = overide_get_db

#     # run our code before we run our test
    
#     yield TestClient(app)

#     # run code before test finishes