from pydantic import BaseModel
from datetime import datetime
class Blog(BaseModel):
    title: str
    body: str
    created_at : datetime