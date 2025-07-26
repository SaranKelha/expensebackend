from fastapi import APIRouter,Depends,Query
from expense import schemas,database,models
from sqlalchemy.orm import Session
from typing import List, Dict
from expense.oaut import get_current_user
from expense.repository import exp

router=APIRouter(
    prefix="/expenses",
    tags=['expenses']
)
@router.post("/", response_model=schemas.Expense, status_code=201)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(database.get_db),current_user: models.User = Depends(get_current_user)):
    return exp.create_expense(expense,db,current_user)

@router.get("/summary/overall", response_model=Dict[str, float])
def get_overall_summary(db: Session = Depends(database.get_db),current_user: models.User = Depends(get_current_user)):
   return exp.get_all_summary(db,current_user.id)

@router.get("/summary/category", response_model=List[schemas.CategorySummary])
def get_summary_by_category(db: Session = Depends(database.get_db),current_user: models.User = Depends(get_current_user)):
    return exp.get_summary_category(db,current_user.id)

@router.get("/summary/time", response_model=List[schemas.TimeSummary])
def get_summary_by_time(
    type: str = Query(..., description="Type of time summary", enum=["day", "week", "month"]),
    db: Session = Depends(database.get_db),current_user: models.User = Depends(get_current_user)
):
    return exp.get_summary_time(type,db,current_user.id)

