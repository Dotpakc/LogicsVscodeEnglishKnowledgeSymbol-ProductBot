import os
import shutil
import json

PRODUCT_FILE = 'data/products.json'



def write_to_file(file_name, data: list):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        return json.load(file)

def check_product_file(name):
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists(name):
        write_to_file(name, [])


def get_products():
    check_product_file(PRODUCT_FILE)
    return read_file(PRODUCT_FILE)


def add_product(data: dict):
    products = get_products()
    products.append(data)
    write_to_file(PRODUCT_FILE, products)
    

    