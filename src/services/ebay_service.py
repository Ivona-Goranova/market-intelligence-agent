from models.product import Product
from models.competitor_product import CompetitorProduct


class EbayService:
    def search_product(self, product: Product) -> list[CompetitorProduct]:
        search_term = product.mpn or product.name

        print(f"🔎 Searching eBay for: {search_term}")

        return [
            CompetitorProduct(
                title=f"eBay result for {search_term}",
                price=19.99,
                seller="ExampleSeller",
                source="eBay",
                link="https://www.ebay.de/"
            )
        ]
    