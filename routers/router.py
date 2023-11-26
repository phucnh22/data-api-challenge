from fastapi import APIRouter

from routers import (
    generic, 
    specific
)

router = APIRouter()

router.include_router(specific.router, tags=["specific"])
router.include_router(generic.router, tags=["generic"])