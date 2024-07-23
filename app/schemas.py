from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class PostBase(BaseModel): # schema/pydantic model: if the user wants to create a post, the request will only go through if it has "title" and "content" in the body
  title: str
  content: str # if str value isn't available, error
  published: bool = True # defaults to true


class PostCreate(PostBase):   
  pass

class Post(PostBase):
  id: int
  created_at: datetime
  class Config:
    from_attributes = True # https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode

class UserBase(BaseModel):
  username: str
  email: EmailStr
  password: str

class UserOut(UserBase):
  password: str = Field(exclude=True)
  id: int
  created_at: datetime
  class Config:
    from_attributes = True # https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode