from urllib.parse import quote_plus

from models.product import Product
from models.competitor_product import CompetitorProduct
from services.ebay_auth_service import EbayAuthService


class EbayService:
    def __init__(self):
        self.auth_service = EbayAuthService()

    def build_search_url(self, product: Product) -> str:
        search_term = product.mpn or product.name
        encoded_search_term = quote_plus(search_term)
        return f"https://www.ebay.de/sch/i.html?_nkw={encoded_search_term}"

    def map_api_item_to_competitor_product(self, item: dict) -> CompetitorProduct:
        price_value = item.get("price", {}).get("value", 0)
        title = item.get("title", "")
        seller = item.get("seller", {}).get("username", "")
        link = item.get("itemWebUrl", "")
        image_url = item.get("image", {}).get("imageUrl", "")

        return CompetitorProduct(
            title=title,
            price=float(price_value),
            shipping_price=0.0,
            sold_quantity=0,
            rating=0.0,
            seller=seller,
            source="eBay",
            link=link,
            image_url=image_url,
        )

    def search_product(self, product: Product) -> list[CompetitorProduct]:
        search_term = product.mpn or product.name
        search_url = self.build_search_url(product)

        print(f"🔎 Searching eBay for: {search_term}")
        print(f"🌐 Search URL: {search_url}")

        dummy_api_response = {
            "itemSummaries": [
                {
                    "title": f"Original Ersatzteil {search_term}",
                    "price": {
                        "value": "19.99",
                        "currency": "EUR"
                    },
                    "seller": {
                        "username": "ExampleSeller"
                    },
                    "itemWebUrl": search_url,
                    "image": {
                        "imageUrl": ""
                    }
                },
                {
                    "title": "Universal Luftfilter",
                    "price": {
                        "value": "15.90",
                        "currency": "EUR"
                    },
                    "seller": {
                        "username": "CheapParts"
                    },
                    "itemWebUrl": search_url,
                    "image": {
                        "imageUrl": ""
                    }
                }
            ]
        }

        return [
            self.map_api_item_to_competitor_product(item)
            for item in dummy_api_response["itemSummaries"]
        ]