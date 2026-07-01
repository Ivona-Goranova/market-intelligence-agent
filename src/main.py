from services.excel_service import ExcelService

print("🚀 Market Intelligence Agent gestartet!")

excel_service = ExcelService()
products = excel_service.read_products("data/ma-products.xlsx")

for product in products:
    print(product)