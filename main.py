# https://aws.amazon.com/what-is/api/#:~:text=API%20stands%20for%20Application%20Programming,other%20using%20requests%20and%20responses.
from typing import Optional, Union
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
  title: str
  content: str # if str value isn't available, error
  published: bool = True # defaults to true
  rating: Optional[int] = None # optional user input, else default to None. if value is not an int, return error 

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


@app.get("/posts")
def get_posts():
  return {"data": "this is your data"}


@app.post("/createposts")
def create_posts(new_post: Post):  # Post will validate that there is a title and content data with str value 
  print(new_post.rating)
  return {"data": "new post"}

# schema