from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from db.database import get_db
from fastapi.datastructures import UploadFile
from .schemas import PostDisplay, PostBase
from sqlalchemy.orm.session import Session
from db import db_post
from typing import List
import random, string, shutil
router = APIRouter(prefix='/post', tags=['post'])

image_url_type = ['absolute', 'relative' ]


@router.post('', response_model=PostDisplay)
def create_post( request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_type:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="it is  unprocessable")
    return db_post.create_post(db, request)



@router.get('/all', response_model=List[PostDisplay])
def get_all_posts( db: Session = Depends(get_db)):
    all_posts = db_post.get_all_posts(db)
    return all_posts

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    random_str = ''.join(random.choice(letter) for i in range(6))
    new = f'_{random_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return  {'filename':path}