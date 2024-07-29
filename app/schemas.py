from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, conint

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


class UserLogin(BaseModel):
  email: EmailStr
  password: str

class PostBase(BaseModel): # schema/pydantic model: if the user wants to create a post, the request will only go through if it has "title" and "content" in the body
  title: str
  content: str # if str value isn't available, error
  published: bool = True # defaults to true

class PostCreate(PostBase):   
  pass

class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int 
  owner: UserOut
  class Config:
    from_attributes = True 
    
class PostVote(BaseModel):
  Post: Post
  votes: int
  class Config:
    from_attributes = True 

    
class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str] = None

class Vote(BaseModel):
  post_id: int
  dir: conint(ge=0, le=1) # type:ignore