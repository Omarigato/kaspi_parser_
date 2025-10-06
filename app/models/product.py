import uuid
from sqlalchemy import Column, String, Text, Float, DECIMAL, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    kaspi_id = Column(String, unique=True, nullable=True)
    kaspi_url = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text)
    rating = Column(Float)
    review_count = Column(Float)
    price = Column(DECIMAL(12, 2))
    created_at = Column(TIMESTAMP, server_default=func.now())


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
    kaspi_image_url = Column(Text, nullable=False)
    is_main = Column(Boolean, default=False)


class Shop(Base):
    __tablename__ = "shops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    kaspi_id = Column(String, unique=True)
    name = Column(Text)
    phone = Column(Text)
    address = Column(Text)


class ShopProduct(Base):
    __tablename__ = "shop_products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_id = Column(UUID(as_uuid=True), ForeignKey("shops.id", ondelete="CASCADE"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
    price = Column(DECIMAL(12, 2))
    availability = Column(Text)
    updated_at = Column(TIMESTAMP, server_default=func.now())


class RelatedProduct(Base):
    __tablename__ = "related_products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
    related_product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
