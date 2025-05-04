from pydantic import BaseModel
from datetime import datetime

class Email(BaseModel):
    subject:str
    sender:str
    body:str
    timestamp:datetime
    is_read:bool = False


    class config:
        orm_mode = True