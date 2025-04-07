from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id : int
    created_at : datetime


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator : Optional[ShowUser]
    
    class Config():
        # orm_mode = True   #-> deprecated
        from_attributes = True