from models.product import Product
from models.competitor_product import CompetitorProduct


class EbayService:
    def search_product(self, product: Product) -> list[CompetitorProduct]:
        search_term = product.mpn or product.name

        print(f"🔎 Searching eBay for: {search_term}")

        return [
            CompetitorProduct(
                title=f"Original Ersatzteil {search_term}",
                price=19.99,
                seller="ExampleSeller",
                source="eBay",
                link="https://www.ebay.de/"
            ),
            CompetitorProduct(
                title="Universal Luftfilter",
                price=15.90,
                seller="CheapParts",
                source="eBay",
                link="https://www.ebay.de/"
            )
        ]
    