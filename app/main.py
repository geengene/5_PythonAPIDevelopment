# https://www.youtube.com/watch?v=0sOvCWFmrtA
# https://aws.amazon.com/what-is/api/#:~:text=API%20stands%20for%20Application%20Programming,other%20using%20requests%20and%20responses.
# https://fastapi.tiangolo.com/tutorial/sql-databases/
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
from fastapi import FastAPI

from app.oauth2 import SECRET_KEY
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
  return "hello world"
    


