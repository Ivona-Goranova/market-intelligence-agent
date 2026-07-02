from urllib.parse import quote_plus

from models.product import Product
from models.competitor_product import CompetitorProduct


class EbayService:
    def build_search_url(self, product: Product) -> str:
        search_term = product.mpn or product.name
        encoded_search_term = quote_plus(search_term)
        return f"https://www.ebay.de/sch/i.html?_nkw={encoded_search_term}"

    def search_product(self, product: Product) -> list[CompetitorProduct]:
        search_url = self.build_search_url(product)
        search_term = product.mpn or product.name

        print(f"🔎 Searching eBay for: {search_term}")
        print(f"🌐 Search URL: {search_url}")

        return [
            CompetitorProduct(
                title=f"Original Ersatzteil {search_term}",
                price=19.99,
                shipping_price=4.99,
                sold_quantity=10,
                rating=4.5,
                seller="ExampleSeller",
                source="eBay",
                link=search_url
            ),
            CompetitorProduct(
                title="Universal Luftfilter",
                price=15.90,
                shipping_price=3.99,
                sold_quantity=5,
                rating=4.0,
                seller="CheapParts",
                source="eBay",
                link=search_url
            )
        ]
    