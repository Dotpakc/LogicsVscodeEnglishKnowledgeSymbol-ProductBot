from loader import dp

from .baseComnds import main_router as base_router
from .admin_module import admin_module
from .user_cabinet import main_router as user_router
from .products import main_router as products_router
from .view_product import main_router as view_product_router

dp.include_router(base_router)
dp.include_router(user_router)
dp.include_router(products_router)
dp.include_router(admin_module)
dp.include_router(view_product_router)

__all__ = ["dp"]