from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(): # async is only used when doing tasks that may take time
    return {"message": "Welcome to NHK"}

@app.get("/posts")
async def get_post():
    return {"data": "This is your post."}