from router.blog_post import required_functionality
from typing import Optional
from fastapi import APIRouter, status, Response, Depends
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

#@myApp.get('/blog/all')
#def get_all_blogs():
# return {'message': 'All blogs provided'}
@router.get('/blog/all',summary='Get all blogs', description='This endpoint returns all blogs', response_description='A list of all blogs')
def get_all_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}

@router.get('/blog/{id}/comments/{comment_id}',tags=['comments'])
def get_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  """
  simulateds retrieving a comment for a blog
  - **id** madatory blog id
  """
  return {'message': f'blog_id {id}, comment_id {comment_id}, valid  {valid}, username {username}'}
 

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
  return {'message': f'Blog type {type}'}

@router.get('/blog/{id}', status_code = status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
      response.status_code = status.HTTP_404_NOT_FOUND
      return {'message': f'Blog {id} not found'}
    else:
      response.status_code = status.HTTP_200_OK
      return {'message': f'Blog with id {id}'}
