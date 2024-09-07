from pydantic import BaseModel


class RouteSchema(BaseModel):
    path: str
    code: int
