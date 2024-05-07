from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
async def root(): # async is only used when doing tasks that may take time
    return {"message": "Welcome to NHK"}

@app.get("/posts")
async def get_post():
    return {"data": "This is your post."}
@app.post("/createposts")
async def post_data(payload: dict = Body(...)):
    print(payload)
    return {"message": "successfully created a post"}