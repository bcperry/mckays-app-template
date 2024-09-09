from pydantic import BaseModel

class ExampleSchema(BaseModel):
    name: str
    age: int
    email: str

    class Config:
        orm_mode = True