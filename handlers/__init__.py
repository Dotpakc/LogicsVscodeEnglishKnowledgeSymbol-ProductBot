from loader import dp

from .baseComnds import main_router as base_router
from .admin_module import admin_module


dp.include_router(base_router)
dp.include_router(admin_module)

__all__ = ["dp"]