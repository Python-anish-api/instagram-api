from fastapi import FastAPI
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles
from routers import user, post, comment
from auth import authentication
from fastapi.middleware.cors import  CORSMiddleware
app = FastAPI()

app.include_router(user.router)
app.include_router(post.router  )
app.include_router(authentication.router)
app.include_router(comment.router)



origins = [
    'http://localhost:3000'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)





app.mount('/images', StaticFiles(directory='images'), name='images')
@app.get("/")
def root():
    return {"message": "Hello World!"}


models.Base.metadata.create_all(engine)