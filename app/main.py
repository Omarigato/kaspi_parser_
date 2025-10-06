from fastapi import FastAPI, HTTPException
from app.services.parser import KaspiParser
from app.core.database import Base, engine, SessionLocal
from app.models.product import Product, ProductImage, Shop, ShopProduct, RelatedProduct

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kaspi Parser API")

@app.post("/parse")
def parse_product(url: str):
    parser = KaspiParser(url)
    data = parser.parse()
    if not data:
        raise HTTPException(status_code=400, detail="Could not parse Kaspi product")

    db = SessionLocal()
    try:
        product = Product(
            kaspi_url=data["kaspi_url"],
            name=data["name"],
            description=data["description"],
            price=data["price"]
        )
        db.add(product)
        db.flush()

        for i, img in enumerate(data["images"]):
            db.add(ProductImage(product_id=product.id, kaspi_image_url=img, is_main=(i == 0)))

        for shop_data in data.get("shops", []):
            shop = Shop(**shop_data)
            db.add(shop)
            db.flush()
            db.add(ShopProduct(shop_id=shop.id, product_id=product.id, price=data["price"], availability="in_stock"))

        for related_url in data.get("related_urls", []):
            related = Product(kaspi_url=related_url, name="Related", description="", price=0)
            db.add(related)
            db.flush()
            db.add(RelatedProduct(product_id=product.id, related_product_id=related.id))

        db.commit()
        db.refresh(product)
        return {"status": "ok", "product_id": str(product.id)}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
