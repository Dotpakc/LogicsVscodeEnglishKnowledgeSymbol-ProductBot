from loader import dp

from .baseComnds import main_router as base_router
from .mymodule import main_router as mymodule_router


dp.include_router(base_router)
dp.include_router(mymodule_router)

__all__ = ["dp"]