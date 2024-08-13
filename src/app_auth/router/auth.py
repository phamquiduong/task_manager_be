from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session

auth_router = APIRouter(prefix='/auth')


@auth_router.get('/health-check')
def health_check():
    return {}


@auth_router.post('/register')
def register(
    session=Annotated[Session, Depends(get_session)]
):
    return {}
