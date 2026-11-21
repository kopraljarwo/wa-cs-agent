from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI(title="WhatsApp AI Customer Service Agent")

class RefundCheckInput(BaseModel):
    order_id: str
    reason: str

def get_order_status(order_id: str) -> dict:
    """Function calling tool: fetch live order status from database."""
    # TODO: Connect to PostgreSQL order table
    return {
        "order_id": order_id,
        "status": "delivered",
        "days_since_delivery": 3,
    }

def check_refund_eligibility(data: RefundCheckInput) -> dict:
    """Function calling tool: validate refund against RAG policy + order state."""
    order = get_order_status(data.order_id)
    eligible = order["days_since_delivery"] <= 7
    return {
        "order_id": data.order_id,
        "eligible": eligible,
        "policy_rule": "Returns accepted within 7 days of delivery with intact packaging.",
    }

@app.get("/webhook/whatsapp")
async def verify_webhook(request: Request):
    params = request.query_params
    if params.get("hub.mode") == "subscribe":
        return int(params.get("hub.challenge", 0))
    raise HTTPException(status_code=403, detail="Verification failed")

@app.post("/webhook/whatsapp")
async def handle_whatsapp_message(request: Request):
    payload = await request.json()
    # TODO: Invoke LangGraph agent (pgvector RAG + tool calling)
    return {"status": "processed", "event": payload}
