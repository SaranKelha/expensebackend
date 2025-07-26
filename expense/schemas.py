from pydantic import BaseModel
from datetime import date
from typing import List,Optional

# Base schema for an expense, contains common fields
class ExpenseBase(BaseModel):
    amount: float
    category: str
    date: date

# Schema for creating a new expense (used in POST request)
class ExpenseCreate(ExpenseBase):
    pass

# Schema for reading an expense (used in GET response)
# Includes fields from the database like 'id'
class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True # This tells Pydantic to read the data even if it is not a dict, but an ORM model

# Base schema for an expense, contains common fields
class ExpenseBase(BaseModel):
    amount: float
    category: str
    date: date
    
# Schema for the category summary
class CategorySummary(BaseModel):
    category: str
    total_amount: float

# Schema for the time-based summary
class TimeSummary(BaseModel):
    period: date # We use date for daily, weekly, and monthly representations
    total_amount: float

class UserCreate(BaseModel):
    name:str
    email: str
    password: str

class UserOut(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True


class TokenData(BaseModel):
    email: Optional[str] = None
    id: Optional[int] = None