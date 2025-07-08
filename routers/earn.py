from fastapi import APIRouter, HTTPException
from models.finance import EarnIn, EarnUpdate
from storage.memory import earns
from services.finance import all_cash_in
from datetime import datetime

router = APIRouter(prefix="/earns", tags=["Earns"])

@router.get("/")
async def get_all_earns():
    return {
        "Earn Operations History": earns,
        "Total Movimented": all_cash_in()
    }

@router.post("/", status_code=201)
async def add_earn(earn: EarnIn):
    earns.append(earn)
    return {"received": earn}

@router.get("/{earn_id}")
async def get_earn_by_id(earn_id: str):
    for earn in earns:
        if earn.id == earn_id:
            return earn
    raise HTTPException(status_code=404, detail="Earn not found")

@router.patch("/{earn_id}")
async def update_earn_by_id(earn_id: str, update_data: EarnUpdate):
    for earn in earns:
        if earn.id == earn_id:
            if update_data.name is not None:
                earn.name = update_data.name
            if update_data.amount is not None:
                earn.amount = update_data.amount
            if update_data.way is not None:
                earn.way = update_data.way
            if update_data.description is not None:
                earn.description = update_data.description
            earn.updated_at = datetime.now()
            return {"message": f"Earn {earn_id} atualizado com sucesso", "data": earn}

    raise HTTPException(status_code=404, detail=f"Earn com id {earn_id} não encontrado")


@router.delete("/{earn_id}")
async def delete_earn_by_id(earn_id: str):
    for index, earn in enumerate(earns):
        if earn_id == earn.id:
            del earns[index]
            return {'message': f'Earn with id {earn.id} deleted!'}
    raise HTTPException(status_code=404, detail="Earn not found!")
