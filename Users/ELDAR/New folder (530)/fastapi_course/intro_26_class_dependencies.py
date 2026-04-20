from fastapi import FastAPI, Depends
from typing import Optional


app = FastAPI()

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0,  limit: int = 100):
        self.q = q 
        self.skip = skip 
        self.limit = limit 


@app.get("/items/")
async def read_items(params: CommonQueryParams = Depends(CommonQueryParams)):
    return {
        "query": params.q,
        "offset":  params.skip,
        "limit": params.limit
    }

@app.get("/users/")
def read_users(params: CommonQueryParams = Depends()):
    return {"message":  "Istifadeciler siyahisi",  "params":  params}


