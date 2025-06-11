from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)
class Image(BaseModel):
    url : str
    alias : str

class BaseModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = [],
    metadata: Dict[str, str,] = {'key': 'val1'},
    image: Optional[Image] = None

@router.post('/new/{id}')
def crate_blog(blog: BaseModel, id: int, version: int = 1):
    return {
        'id' : id,        
        'data' : blog,
        'version' : version
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BaseModel, 
                    id: int, 
                   comment_title: int = Query(None,
                   title = 'title of the comments',
                   description = 'descrioption of the comment title',
                   alias = 'commentId',
                   deprecated = True
                   ),
                   content: str = Body(...,
                   max_length = 10,
                   min_length = 1,
                   regex = '^[a-z\s]*$'),
                   v : Optional[List[str]] = Query(['1.0','1.1','1.2']),
                   comment_id : int = Path(..., gt = 5, le = 10)
                   ):
    return {
        'id' : id,
        'data' : blog,
        'comment_title' : comment_title,
        'content' : content,
        'version' : v,
        'comment_id' : comment_id
    }

def required_functionality():
  return {'message': 'Learning FastAPI is important'}