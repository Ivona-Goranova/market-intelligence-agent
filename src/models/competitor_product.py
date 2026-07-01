from dataclasses import dataclass


@dataclass
class CompetitorProduct:
    title: str
    price: float
    seller: str
    source: str
    link: str

    