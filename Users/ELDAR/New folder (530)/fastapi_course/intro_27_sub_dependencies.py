from fastapi import FastAPI,  Depends, Cookie,  HTTPException 

app = FastAPI()


def query_extractor(q:  str | None = None):
    return q 


def query_or_cookie_extractor(q: str = Depends(query_extractor),  last_query: str | None = Cookie(None)):
    if not q:
        return last_query
    return q 


@app.get("/items/")
async def read_query(active_query: str = Depends(query_or_cookie_extractor)):
    return {"active_query":  active_query}

