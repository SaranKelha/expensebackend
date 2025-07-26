from passlib.context import CryptContext

pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")
class Hash():
    def bcrypt(password:str):
        return pwd.hash(password)
    
    def verify(plainpassword,hashpassword):
        return pwd.verify(plainpassword,hashpassword)