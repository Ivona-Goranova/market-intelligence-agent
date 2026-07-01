from services.excel_service import ExcelService
from services.ebay_service import EbayService

print("🚀 Market Intelligence Agent gestartet!")

excel_service = ExcelService()
ebay_service = EbayService()

products = excel_service.read_products("data/ma-products.xlsx")

for product in products:
    print("\n📦 MA product:")
    print(product)

    ebay_results = ebay_service.search_product(product)

    print("🛒 eBay results:")
    for result in ebay_results:
        print(result)
        