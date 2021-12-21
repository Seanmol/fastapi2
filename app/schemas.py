from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from pydantic.networks import EmailStr
from pydantic.types import conint

class Post(BaseModel):
    title:str
    content:str
    published:bool = True   


class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode = True


class PostResponse(PostBase):

    id:int
    created_at: datetime
    owner:UserOut

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email:EmailStr
    password:str
    
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email:EmailStr
    password: str


class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    id:Optional[str] = None


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)

class PostOut(BaseModel):
    Post:PostResponse
    votes:int

    class Config:
        orm_mode=True