from sqlmodel import SQLModel, Field
from typing import Optional

class HelloBase(SQLModel):
    world: str

class Hello(HelloBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class HelloOut(HelloBase):
    id: int