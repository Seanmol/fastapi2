from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):

    old_user = db.query(models.User).filter(models.User.email == user.email).first()

    if old_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Users with email: {user.email} already exist")
    
    hashed_password = utils.hasher(user.password)
    user.password = hashed_password

    new_user =  models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")

    return user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db:Session= Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.id == id)

    if not user_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} is doesn't exist.")

    user_query.delete(synchronize_session=False)
    db.commit()
