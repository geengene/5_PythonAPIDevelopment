from typing import Union

from fastapi import Body, FastAPI

app = FastAPI()


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
    return {"data":"this is your data"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)): # extracts all the fields from the body, convert it to a python dictionary and store it inside variable "payload"
    print(payload) 
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}

