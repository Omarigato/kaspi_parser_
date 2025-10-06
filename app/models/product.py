from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    rating = Column(Float, nullable=True)
    reviews = Column(Integer, nullable=True)
