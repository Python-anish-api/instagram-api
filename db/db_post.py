from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from routers.schemas import PostBase
from  db.models import DbPost
import datetime
def create_post(db:Session, request: PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db:Session):
    return db.query(DbPost).all()



def delete_post(db:Session, id:int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user with the post not found')
    if post.user_id  !=  user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='only post owner can delete')
    
    db.delete(post)
    db.commit()
    return 'ok'