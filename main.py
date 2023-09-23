from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from auth.views import router as auth_router
from items.views import router as items_router
from asset_stacks.views import router as depot_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(items_router, prefix="/items")
app.include_router(depot_router, prefix="/depot")

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    # TODO: get app url from .env
    # FEATURE: add envoirement var for features like debug and reload
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
