from models.product import Product
from models.competitor_product import CompetitorProduct


class MatchingService:

    def is_match(
        self,
        product: Product,
        competitor: CompetitorProduct
    ) -> bool:

        title = competitor.title.lower()

        if product.mpn.lower() in title:
            return True

        if product.name.lower() in title:
            return True

        return False
    
    