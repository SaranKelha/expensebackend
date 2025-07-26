from sqlalchemy.orm import Session
from expense import models,schemas,hashing



def create(request:schemas.UserCreate,db:Session):
    
    newuser = models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

def getall(db:Session):
    users = db.query(models.User).all()
    return users