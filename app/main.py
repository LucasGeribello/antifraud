from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from app.logic import evaluate_transaction

app = FastAPI()

class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    transaction_date: str
    amount: float
    location: str
    device: str

@app.post("/check_transaction")
def check_transaction(transaction: Transaction):
    decision = evaluate_transaction(transaction)
    return {
        "transaction_id": transaction.transaction_id,
        "user_id": transaction.user_id,
        "decision": decision
    }
