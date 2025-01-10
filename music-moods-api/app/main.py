from typing import Union

from fastapi import FastAPI

from .routers import recommendations

app = FastAPI()

app.include_router(recommendations.router)

@app.get("/")
async def read_root() -> Union[dict, str]:
    return {"message": "HI! THERE!"}