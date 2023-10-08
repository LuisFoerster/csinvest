from pydantic import BaseModel

class VendorBase(BaseModel):
    id: int
    name: str
    provision: float
    icon_url: str