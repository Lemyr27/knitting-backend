from fastapi import APIRouter

from app.api.details import create_detail, update_detail, delete_detail

router = APIRouter(prefix='/details', tags=['details'])

router.add_api_route('', create_detail, methods=['POST'])
router.add_api_route('/{id}', update_detail, methods=['PATCH'])
router.add_api_route('/{id}', delete_detail, methods=['DELETE'])
