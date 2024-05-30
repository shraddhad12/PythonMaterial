import asyncio
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def get_data():
    return {"data": "real async data"}

@app.get("/async-data")
async def read_async_data(data: dict = Depends(get_data)):
    return data