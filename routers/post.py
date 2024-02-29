from fastapi import APIRouter, Depends
from db.database import get_db
from .schemas import PostDisplay, PostBase
from sqlalchemy.orm.session import Session
router = APIRouter(prefix='/post', tags=['post'])

image_url_type = ['absolute', 'relative' ]

@router.post('', response_model=PostDisplay)
def create_post( request: PostBase, db: Session = Depends(get_db)):
    pass