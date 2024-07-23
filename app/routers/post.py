from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/posts", response_model=List[schemas.Post]) # retreiving preexisting posts from server to user
def get_posts(db: Session = Depends(get_db)):
  # cur.execute("""SELECT * FROM posts;""")
  # posts = cur.fetchall()
  posts = db.query(models.Post).all()
  return posts # sends posts back to user


@router.get("/posts/{id}", response_model=schemas.Post) # path parameter
def get_post(id: int, db: Session = Depends(get_db)): # validates that id is an integer. no longer necessary to convert to integer by ourselves.
  # cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
  # post = cur.fetchone()
  post = db.query(models.Post).filter(models.Post.id == id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
  return post


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)  # user to server. ensure that the response conforms to the specified model in return
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):  # Post will validate that there is a title and content data with str value in the Body, when creating an entity, return a 201 status 
  # cur.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
  # new_post = cur.fetchone()
  # conn.commit() # this will save the data to postgres database
  # new_post = models.Post(title=post.title, content=post.content, published=post.published)
  new_post = models.Post(**post.model_dump()) # unpacks post into dictionary does the same as above
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
  # cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
  # deleted_post = cur.fetchone()
  # conn.commit()
  deleted_post = db.query(models.Post).filter(models.Post.id == id)
  if deleted_post.first() == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
  deleted_post.delete(synchronize_session=False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT) # data shouldnt be sent back

@router.put("/posts/{id}", response_model=schemas.Post) # updates data received from user
def update_post(id: int, post: schemas.PostBase, db: Session = Depends(get_db)):
  # cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id),))
  # updated_post = cur.fetchone()
  # conn.commit()
  post_query = db.query(models.Post).filter(models.Post.id == id)
  updated_post = post_query.first()
  if updated_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
  post_query.update(dict(post), synchronize_session=False)
  db.commit()
  return post_query.first()