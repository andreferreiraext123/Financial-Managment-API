from fastapi import FastAPI
from routers import earn, expense
from services.finance import saved_money, all_cash_in, all_cash_out

app = FastAPI(title="Controle Financeiro", version="1.0.0")

app.include_router(earn.router)
app.include_router(expense.router)

@app.get("/wallet")
async def get_wallet():
    return {
        "wallet": f"The saved amount is R$ {saved_money()}",
        "Amount Out": f"The total movimented out R$ {all_cash_out()}",
        "Amount In": f"The total movimented in R$ {all_cash_in()}"
    }
