from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session= Depends(database.get_db)):
    return user.create(request, db)
    

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(database.get_db)):
    return user.show(id, db)