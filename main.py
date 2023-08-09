from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from auth.views import router as auth_router
from items.views import router as items_router
from asset_stacks.views import router as depot_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(items_router, prefix="/items")
app.include_router(depot_router, prefix="/depot" )

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
