from fastapi import FastAPI, Body
from datetime import datetime, time, timedelta
from uuid import UUID, uuid4 
from typing import Optional


app = FastAPI()

@app.post("/orders/{order_id}")
async def process_order(order_id: UUID, start_datetime: Optional[datetime] = Body(None), end_date: Optional[datetime] = Body(None), repeat_at: Optional[time] = Body(None), process_after: Optional[timedelta] = Body(None)):
    actual_duration = end_date - start_datetime if end_date and start_datetime else None 

    return {
        "order_id": order_id,
        "start_datetime": start_datetime,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "actual_duration": actual_duration
    }