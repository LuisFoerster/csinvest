from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from data_service.auth.views import router as auth_router
from web_service.shop.views import router as shop_router
from web_service.asset_stacks.views import router as depot_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(shop_router, prefix="/shop")
app.include_router(depot_router, prefix="/depot")

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://192.168.179.3:8000"
    "http://192.168.179.11",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




if __name__ == "__main__":
    # TODO: get app url from .env
    # FEATURE: add envoirement var for features like debug and reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
