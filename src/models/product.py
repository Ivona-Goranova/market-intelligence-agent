from dataclasses import dataclass


@dataclass
class Product:
    article_number: str
    ean: str
    mpn: str
    name: str
    manufacturer: str
    category: str
    description: str
    ma_price: float
    image_url: str
    link: str