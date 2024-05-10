from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()

class Post(BaseModel): # checks the mentioned values to see if they are following the datatype
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "some content",  "id": 1}, {
    "title": "my favourite food", "content": "my favourite food is", "id": 2
}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root(): # async is only used when doing tasks that may take time
    return {"message": "Welcome to NHK"}

@app.get("/posts")
async def get_post():
    return {"data": my_posts}

@app.post("/posts")
async def post_data(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": my_posts}


@app.get('/posts/{id}')
def get_post(id):
    post = find_post(id)
    return {"post_detail": f"here is the post {id}"}