from fastapi import APIRouter

from app.api.healthcheck import healthcheck
from app.routers.user import router as user_router
from app.routers.post import router as post_router

router = APIRouter(prefix='/api/v1')

router.include_router(user_router)
router.include_router(post_router)

router.add_api_route('/healthcheck', healthcheck, methods=['GET'])
