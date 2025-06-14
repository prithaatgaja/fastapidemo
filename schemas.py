from typing import List
from pydantic import BaseModel

#Article inside the userDisplay
class Article(BaseModel):
  title: str
  content: str
  published: bool

#User inside the articleDisplay
class User(BaseModel):
  id: int
  username: str
  class Config():
    orm_mode = True


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  items: List[Article] = []
  class Config():
    orm_mode = True
  
class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int

class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: User
  class Config():
    orm_mode = True