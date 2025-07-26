from fastapi import APIRouter,Depends,HTTPException,status

from expense.hashing import Hash
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from expense import database

from expense import models
from expense import autoken


router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invaild Credentials")
    if not Hash.verify(request.password,user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
     #generate a jwt token and return
    
    access_token = autoken.create_access_token(
        data={"sub": user.email,"id": user.id})
    return {"access_token":access_token, "token_type":"bearer"}
            


