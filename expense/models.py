from sqlalchemy import Column, Integer, String, Float, Date,ForeignKey
from expense.database import Base
from sqlalchemy.orm import relationship

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, index=True, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User",back_populates="expenses")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    expenses = relationship("Expense", back_populates="user")
