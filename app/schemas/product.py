from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    min_price: float | None
    max_price: float | None
    rating: float | None
    reviews: int | None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
