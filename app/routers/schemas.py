from fastapi import APIRouter

from app.api.schemas import get_schemas, get_schema, create_schema, update_schema, delete_schema

router = APIRouter(prefix='/schemas', tags=['schemas'])

router.add_api_route('', get_schemas, methods=['GET'])
router.add_api_route('/{id}', get_schema, methods=['GET'])
router.add_api_route('', create_schema, methods=['POST'])
router.add_api_route('/{id}', update_schema, methods=['PATCH'])
router.add_api_route('/{id}', delete_schema, methods=['DELETE'])
