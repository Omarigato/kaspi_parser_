import json
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import Base, engine, get_db
from app.models.product import Product
from app.schemas.product import ProductResponse
from app.services.parser import parse_product

app = FastAPI(title="Kaspi Parser")

Base.metadata.create_all(bind=engine)

@app.get("/parse", response_model=ProductResponse)
def parse(db: Session = Depends(get_db)):
    url = json.load(open("seed.json"))["product_url"]
    data = parse_product(url)
    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
