# https://www.youtube.com/watch?v=0sOvCWFmrtA
# https://aws.amazon.com/what-is/api/#:~:text=API%20stands%20for%20Application%20Programming,other%20using%20requests%20and%20responses.
# https://fastapi.tiangolo.com/tutorial/sql-databases/
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
from typing import List
from xml.etree.ElementInclude import include
from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


try:
  conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='0490258', cursor_factory=RealDictCursor)
  cur = conn.cursor()
  print("Connection to database successful")
except Exception as error:
  print("Connection failed\nError:", error)

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def read_root():
  return "hello world"
    


