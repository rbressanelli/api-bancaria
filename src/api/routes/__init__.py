from fastapi import APIRouter

from src.api.routes.accounts import router as accounts_router
from src.api.routes.auth import router as auth_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(accounts_router)
