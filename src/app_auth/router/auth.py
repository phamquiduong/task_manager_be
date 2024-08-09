from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')


@auth_router.get('/health-check')
def health_check():
    return {}
