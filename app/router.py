from fastapi import APIRouter

from app.api.healthcheck import healthcheck
from app.routers.users import router as user_router
from app.routers.posts import router as post_router
from app.routers.schemas import router as schema_router
from app.routers.details import router as detail_router
from app.routers.categories import router as category_router

router = APIRouter(prefix='/api/v1')

router.include_router(user_router)
router.include_router(post_router)
router.include_router(schema_router)
router.include_router(detail_router)
router.include_router(category_router)

router.add_api_route('/healthcheck', healthcheck, methods=['GET'])
