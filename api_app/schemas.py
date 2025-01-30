from pydantic import BaseModel


class ImeiIn(BaseModel):
    """Schema for IMEI verification input."""

    imei: str = None
    token: str = None

class ImeiOut(BaseModel):
    """Schema for IMEI verification output."""

    status: int
    result: dict