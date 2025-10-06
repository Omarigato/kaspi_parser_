import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

EXPORT_PATH = Path("export/product.json")

def parse_product(url: str) -> dict:
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    name = soup.select_one("h1[itemprop='name']").get_text(strip=True)
    category = soup.select_one("a.breadcrumbs__link").get_text(strip=True)
    rating = soup.select_one("span[itemprop='ratingValue']")
    reviews = soup.select_one("span[itemprop='reviewCount']")
    prices = [int(p.get_text(strip=True).replace("₸", "").replace(" ", "")) for p in soup.select(".item__price")]

    data = {
        "name": name,
        "category": category,
        "min_price": min(prices) if prices else None,
        "max_price": max(prices) if prices else None,
        "rating": float(rating.text) if rating else None,
        "reviews": int(reviews.text) if reviews else None
    }

    EXPORT_PATH.parent.mkdir(exist_ok=True)
    EXPORT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=4))
    return data
