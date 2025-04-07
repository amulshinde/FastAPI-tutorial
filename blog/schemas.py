from pydantic import BaseModel
from datetime import datetime
<<<<<<< HEAD
from typing import List, Optional
=======
from typing import List
>>>>>>> d93d0e02ba9eb9775095fd6b1e15962c63a48fa1

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