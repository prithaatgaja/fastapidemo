
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from exceptions import StoryException
from fastapi import FastAPI
from router import blog_get, blog_post, user, article, product, file
from auth import authentication
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


myApp = FastAPI()
myApp.include_router(authentication.router)
myApp.include_router(file.router)
myApp.include_router(user.router)
myApp.include_router(article.router)
myApp.include_router(product.router)
myApp.include_router(blog_get.router)
myApp.include_router(blog_post.router)


@myApp.get('/hello')
def index():
  return {'message': 'Hello world!'}

@myApp.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(
    status_code=418,
    content={'details': exc.name }
    )

#@myApp.exception_handler(HTTPException)
#def custom_handler(request: Request, exc: StoryException):
#  return PlainTextResponse(str(exc), status_code=400) 

models.Base.metadata.create_all(engine)

origin = ['https://ideal-dollop-gx6ggggv5v9fvjjq-8000.app.github.dev']



myApp.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
myApp.mount('/files', StaticFiles(directory="files"), name="files")


  
   