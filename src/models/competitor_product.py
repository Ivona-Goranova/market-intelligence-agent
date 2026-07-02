from dataclasses import dataclass


@dataclass
class CompetitorProduct:
    title: str
    price: float
    seller: str
    source: str
    link: str
    shipping_price: float = 0.0
    image_url: str = ""
    sold_quantity: int = 0
    rating: float = 0.0
    