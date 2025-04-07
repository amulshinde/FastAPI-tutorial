from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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
    blogs: List

    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    # creator : Optional[str]
    
    class Config():
        # orm_mode = True   #-> deprecated
        from_attributes = True