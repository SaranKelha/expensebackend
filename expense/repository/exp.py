from fastapi import HTTPException,status
from expense import schemas,models
from sqlalchemy.orm import Session
from sqlalchemy import func



def create_expense(expense: schemas.ExpenseCreate, db: Session ,current_user: models.User):
    """
    Add a new expense.
    """
    db_expense = models.Expense(amount=expense.amount, category=expense.category, date=expense.date,user_id=current_user.id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_all_summary(db: Session,user_id: int):
    """
    Get the total overall spending.
    """
    total_spending = db.query(func.sum(models.Expense.amount)).filter(models.Expense.user_id == user_id).scalar()
    return {"total_expense": total_spending or 0.0}

def get_summary_category(db: Session,user_id: int):
    """
    Get spending summarized by category.
    """
    summary = db.query(
        models.Expense.category,
        func.sum(models.Expense.amount).label("total_amount")
    ).filter(models.Expense.user_id == user_id).group_by(models.Expense.category).all()
    
    return [{"category": cat, "total_amount": total} for cat, total in summary]

def get_summary_time(
    type: str ,db: Session,user_id: int):
    """
    Get spending summarized over time (daily, weekly, or monthly).
    """
    if type not in ["day", "week", "month"]:
        raise HTTPException(status_code=400, detail="Invalid summary type. Choose 'day', 'week', or 'month'.")
    
    # Use date_trunc to group by the specified time period
    summary = db.query(
        func.date_trunc(type, models.Expense.date).label("period"),
        func.sum(models.Expense.amount).label("total_amount")
    ).filter(models.Expense.user_id == user_id).group_by("period").order_by("period").all()

    return [{"period": period.date(), "total_amount": total} for period, total in summary]


