from services.excel_service import ExcelService
from services.ebay_service import EbayService
from services.matching_service import MatchingService
from services.result_export_service import ResultExportService

print("🚀 Market Intelligence Agent gestartet!")

excel_service = ExcelService()
ebay_service = EbayService()
matching_service = MatchingService()
export_service = ResultExportService()

products = excel_service.read_products("data/ma-products.xlsx")

matches = []

for product in products:
    print("\n📦 MA product:")
    print(product)

    ebay_results = ebay_service.search_product(product)

    for result in ebay_results:
        print(result)

        if matching_service.is_match(product, result):
            print("✅ MATCH")
            matches.append((product, result))
        else:
            print("❌ NO MATCH")

export_service.export_matches("data/results.xlsx", matches)

print("\n📊 Results exported to data/results.xlsx")
