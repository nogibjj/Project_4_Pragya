from pydantic import BaseModel

class Item(BaseModel):
    task: str
    status:str