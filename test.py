from utils.files import get_all_categories, get_products_by_category

def print_result(result):
    for key, value in result.items():
        print(value.get("name"), value.get("price"), value.get("category"))

categories = get_all_categories()
print(categories)
products = get_products_by_category(categories.pop())
print_result(products)
print("=====================================")
products = get_products_by_category(categories.pop())
print_result(products)
print("=====================================")