from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root() -> Union[dict, str]:
    return {"Hello": "World"}