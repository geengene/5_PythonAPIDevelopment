# https://aws.amazon.com/what-is/api/#:~:text=API%20stands%20for%20Application%20Programming,other%20using%20requests%20and%20responses.
from typing import Optional, Union
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
  title: str
  content: str # if str value isn't available, error
  published: bool = True # defaults to true
  rating: Optional[int] = None # optional user input, else default to None. if value is not an int, return error 

my_posts = [{"title": "title 1", "content": "content 1", "id": 1}, 
            {"title": "title 2", "content": "content 2", "id": 2}] 

def find_post(id):
  for p in my_posts:
    if p["id"] == id:
      return p

@app.get("/")
def read_root():
  return {"Hello": "Worldiiiii"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

# You already created an API that:

# Receives HTTP requests in the paths / and /items/{item_id}.
# Both paths take GET operations (also known as HTTP methods).
# The path /items/{item_id} has a path parameter item_id that should be an int.
# The path /items/{item_id} has an optional str query parameter q.


@app.get("/posts") # retreiving preexisting posts from server to user
def get_posts():
  return {"data": my_posts} # sends my_posts back to user


@app.post("/posts", status_code=status.HTTP_201_CREATED) # user to server
def create_posts(post: Post):  # Post will validate that there is a title and content data with str value, when creating an entity, return a 201 status
  post_dict = post.model_dump()
  post_dict['id'] = randrange(0, 100000000)
  my_posts.append(post_dict) # adds post post_dict in Body(Postman) to array my_posts
  return {"data": post_dict}

@app.get("/posts/{id}") # path parameter
def get_post(id: int): # response: Response): # validates that id is an integer. no longer necessary to convert to integer by ourselves.
  post = find_post(id) # id passed from get_post is a string as the path parameter
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"message": f"post with id:{id} not found"}
  return {"post_detail": post}

# @app.get("posts/latest")