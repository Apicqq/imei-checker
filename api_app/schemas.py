from pydantic import BaseModel


class ImeiIn(BaseModel):
    imei: str = None
    token: str = None