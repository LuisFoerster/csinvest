from fastapi import FastAPI

from auth.views import router as auth_router
from items.views import router as items_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(items_router, prefix="/items")

