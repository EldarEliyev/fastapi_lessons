from fastapi import FastAPI

app = FastAPI()

def logic_error_calculation(x: int):
    y = x + 10
    z = y * 2
    return y 

@app.get("/debug-test/{number}")
async def debug_test(number: int):
    result = logic_error_calculation(number)
    return {"original": number, "calculated_result": result}