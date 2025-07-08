from decimal import Decimal
from storage.memory import earns, expenses

def all_cash_in():
    total = 0
    for earn in earns:
        total += earn.amount
    return total

def all_cash_out():
    total = 0
    for expense in expenses:
       total += expense.amount
    return total

def saved_money():
    return all_cash_in() - all_cash_out()