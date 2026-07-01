from openpyxl import Workbook

from models.product import Product
from models.competitor_product import CompetitorProduct


class ResultExportService:
    def export_matches(
        self,
        file_path: str,
        matches: list[tuple[Product, CompetitorProduct]]
    ) -> None:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Konkurrenzdaten"

        sheet.append([
            "MA Artikelnummer",
            "MA Produktname",
            "MA Preis",
            "Quelle",
            "Konkurrenzprodukt",
            "Konkurrenzpreis",
            "Verkäufer",
            "Link"
        ])

        for product, competitor in matches:
            sheet.append([
                product.article_number,
                product.name,
                product.ma_price,
                competitor.source,
                competitor.title,
                competitor.price,
                competitor.seller,
                competitor.link
            ])

        workbook.save(file_path)
        