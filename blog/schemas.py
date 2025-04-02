from pydantic import BaseModel
from datetime import datetime

class Blog(BaseModel):
    title: str
    body: str
    created_at : datetime


class ShowBlog(BaseModel):
    title: str
    body: str
    class Config():
        # orm_mode = True   #-> deprecated
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str