from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from uuid import UUID


class ProductImageSchema(BaseModel):
    kaspi_image_url: HttpUrl
    is_main: bool = False


class ShopSchema(BaseModel):
    kaspi_id: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    address: Optional[str]


class ShopProductSchema(BaseModel):
    price: float
    availability: str


class ProductCreateSchema(BaseModel):
    kaspi_url: HttpUrl
    name: str
    description: Optional[str]
    price: float
    images: List[ProductImageSchema]
    shops: Optional[List[ShopSchema]] = []
    related_urls: Optional[List[HttpUrl]] = []
