import uuid
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.SourceResponse)
def create_post(post: schemas.CreateSourceSchema, db: Session = Depends(get_db)):
    frequency = (post.to_date- post.from_date).total_seconds()/60
    frequency_min = str(int(frequency)) + "M"
    new_source = models.Source(**post.dict())
    new_source.frequency = frequency_min
    db.add(new_source)
    db.commit()
    db.refresh(new_source)
    return new_source


@router.put('/')
def update_post(post: schemas.UpdateSourceSchema, db: Session = Depends(get_db)):
    
    post_query = db.query(models.Source).filter(models.Source.source_id == post.source_id)
    updated_post = post_query.first()
    updated_post_dict = post.dict()
    updated_frequency = (post.to_date-post.from_date).total_seconds()/60
    updated_frequency_min = str(int(updated_frequency))+"M"
    updated_post_dict["frequency"] = updated_frequency_min
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No source with this id: {id} found')
    post_query.update(updated_post_dict, synchronize_session=False)
    db.commit()
    return {"status":"success"}

@router.get('/{id}', response_model=schemas.SourceResponse)
def get_post(id: str, db: Session = Depends(get_db)):
    post = db.query(models.Source).filter(models.Source.source_id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No post with this id: {id} found")
    return post
