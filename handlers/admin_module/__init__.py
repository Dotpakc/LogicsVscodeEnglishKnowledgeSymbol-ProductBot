from aiogram import Router

from .admin import admin_router
from .add_product import add_product_router

admin_module = Router()

admin_module.include_router(admin_router)
admin_module.include_router(add_product_router)
