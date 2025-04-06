from fastapi import FastAPI
from app.init_db import init_db
from app.routes import domain_routes

app = FastAPI()

app.include_router(domain_routes.router)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
def read_root():
    return {"message": "DomainLookup API is running."}
