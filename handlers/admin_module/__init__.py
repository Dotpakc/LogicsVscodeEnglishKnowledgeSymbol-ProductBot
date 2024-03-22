from aiogram import Router

from .admin import admin_router
from .add_product import add_product_router
from .list_product import list_product_router
from .del_product import del_product_router

admin_module = Router()

admin_module.include_router(admin_router)
admin_module.include_router(add_product_router)
admin_module.include_router(list_product_router)
admin_module.include_router(del_product_router)