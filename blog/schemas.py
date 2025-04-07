from pydantic import BaseModel
from datetime import datetime
from typing import List

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

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True