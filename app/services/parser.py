import requests
from bs4 import BeautifulSoup

class KaspiParser:
    def __init__(self, url: str):
        self.url = url

    def parse(self) -> dict:
        response = requests.get(self.url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            return {}

        soup = BeautifulSoup(response.text, "html.parser")
        name = soup.select_one("h1").get_text(strip=True) if soup.select_one("h1") else "Unknown"
        description = soup.select_one("meta[name='description']")
        price_el = soup.select_one(".price")
        description_text = description["content"] if description else ""
        price = float(price_el.get_text(strip=True).replace("₸", "").replace(" ", "")) if price_el else 0.0
        images = [img["src"] for img in soup.select("img") if "kaspi.kz" in img["src"]]

        return {
            "kaspi_url": self.url,
            "name": name,
            "description": description_text,
            "price": price,
            "images": images[:5],  # ограничим
        }
