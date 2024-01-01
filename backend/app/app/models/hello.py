from sqlmodel import SQLModel, Field
from typing import Optional

class HelloBase(SQLModel):
    world: str

class Hello(HelloBase, table=true):
    id: Optional[int] = Field(default=None, primary_key=True)