from fastapi import APIRouter,Depends
from expense import database,schemas
from sqlalchemy.orm import Session
from expense.repository import user


router=APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/')
def create(request:schemas.UserCreate,db:Session = Depends(database.get_db)):
    return user.create(request,db)

@router.get('/',response_model=list[schemas.UserOut])
def all(db:Session = Depends(database.get_db)):
    return user.getall(db)
