from fastapi import FastAPI
from expense.router import exp,user
from expense.router import authentication
# Import local modules
from  expense import models
from expense.database import engine
from fastapi.middleware.cors import CORSMiddleware

# Create all database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API", description="API for tracking personal expenses", version="1.0.0")



app.include_router(exp.router)
app.include_router(user.router)
app.include_router(authentication.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify: ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





