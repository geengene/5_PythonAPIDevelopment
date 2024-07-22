# https://aws.amazon.com/what-is/api/#:~:text=API%20stands%20for%20Application%20Programming,other%20using%20requests%20and%20responses.
# https://fastapi.tiangolo.com/tutorial/sql-databases/
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


try:
  conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='0490258', cursor_factory=RealDictCursor)
  cur = conn.cursor()
  print("Connection successful")
except Exception as error:
  print("Connection failed\nError:", error)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
  return {"Hello": "Worldiiiii"}

class Post(BaseModel):
  title: str
  content: str # if str value isn't available, error
  published: bool = True # defaults to true

    
@app.get("/posts") # retreiving preexisting posts from server to user
def get_posts():
  cur.execute("""SELECT * FROM posts;""")
  posts = cur.fetchall()
  return {"data": posts} # sends posts back to user

@app.post("/posts", status_code=status.HTTP_201_CREATED)  # user to server
def create_posts(post: Post):  # Post will validate that there is a title and content data with str value in the Body, when creating an entity, return a 201 status 
  cur.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
  new_post = cur.fetchone()
  conn.commit() # this will save the data to postgres database
  return {"data": new_post}

@app.get("/posts/{id}") # path parameter
def get_post(id: int): # response: Response): # validates that id is an integer. no longer necessary to convert to integer by ourselves.
  cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
  post = cur.fetchone()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
  return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
  deleted_post = cur.fetchone()
  conn.commit()
  if deleted_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
  return Response(status_code=status.HTTP_204_NO_CONTENT) # data shouldnt be sent back

@app.put("/posts/{id}") # updates data received from user
def update_post(id: int, post:Post):
  cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id),))
  updated_post = cur.fetchone()
  conn.commit()
  if updated_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
  return {"data": updated_post}