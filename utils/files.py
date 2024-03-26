import os
import shutil
import json





def write_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        return json.load(file)

def check_file(name):
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists(name):
        write_to_file(name, {})



## Products

PRODUCT_FILE = 'data/products.json'

def get_products():
    check_file(PRODUCT_FILE)
    return read_file(PRODUCT_FILE)


def add_product(data: dict):
    products = get_products()
    products[data.get("id")] = data
    write_to_file(PRODUCT_FILE, products)
    

def find_product(product_id):
    products = get_products()
    return products.get(product_id)
    

def del_product(product_id):
    products = get_products()
    if product_id in products:
        del products[product_id]
        write_to_file(PRODUCT_FILE, products)
        return True
    return False

## Users
USERS_FILE = 'data/users.json'

# "123":{
#     id: 123,
#     cart: [1, 2, 3] # product_id
#     orders: [ 1,5,6] # order_id
#     bonus: 100
# },
# "124":{
#     id: 124,
#     cart: [1, 2, 3] # product_id
#     orders: [ 1,5,6] # order_id
#     bonus: 100
# }


def get_users():
    check_file(USERS_FILE)
    return read_file(USERS_FILE)

def add_user(data: dict):
    users = get_users()
    users[str(data.get("id"))] = data
    write_to_file(USERS_FILE, users)
    
def find_user(user_id):
    users = get_users()
    return users.get(str(user_id), None)


def change_user(user_id, data):
    users = get_users()
    if str(user_id) in users:
        print("change_user", data)
        users[str(user_id)] = data
        write_to_file(USERS_FILE, users)
        return True
    return False

def get_or_create_user(user_id):
    user = find_user(user_id)
    if not user:
        user = {
            "id": user_id,
            "cart": ["d9939f1b40884c33a50992d3da274b94","c0067648eaa548ba823dd988fe11c7ed"],
            "orders": [],
            "bonus": 0
        }
        add_user(user)
        return user, True
    return user, False

def get_user_cart(user_id):
    user, _  = get_or_create_user(user_id)
    if user:
        new_cart = []
        cart = user.get("cart", [])
        for product_id in cart:
            product = find_product(product_id)
            if product:
                new_cart.append(product)
        return new_cart
