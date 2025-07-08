from fastapi import APIRouter, HTTPException
from models.finance import ExpenseIn, ExpenseUpdate
from storage.memory import expenses
from services.finance import all_cash_out
from datetime import datetime

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.get("/")
async def get_all_expenses():
    return {
        "Expense Operations History": expenses,
        "Total Movimented": all_cash_out()
    }

@router.post("/", status_code=201)
async def add_expense(expense: ExpenseIn):
    expenses.append(expense)
    return {"received": expense}

@router.get("/{expense_id}")
async def get_expense_by_id(expense_id: str):
    for expense in expenses:
        if expense.id == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")

@router.patch("/{expense_id}")
async def update_expense_by_id(expense_id: str, update_data: ExpenseUpdate):
    for expense in expenses:
        if expense.id == expense.id:
            if update_data.name is not None:
                expense.name = update_data.name
            if update_data.amount is not None:
                expense.amount = update_data.amount
            if update_data.way is not None:
                expense.way = update_data.way
            if update_data.description is not None:
                expense.description = update_data.description
            
            expense.updated_at = datetime.now()
            return {'message': f'Expense {expense_id} atualizado com sucesso', 'data': expense}
    raise HTTPException(status_code=404, detail=f'Expense with ID {expense_id} not found') 

@router.delete("/{expense_id}")
async def delete_expense_by_id(expense_id: str):
    for index, expense in enumerate(expenses):
        if expense_id == expense.id:
            del expenses[index]
            return {'message': f'Expense with id {expense.id} was deleted!'}
    raise HTTPException(status_code=404, detail="Expense not found!")    
