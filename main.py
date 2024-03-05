from fastapi import FastAPI
from src.routes.user import data

app = FastAPI(
    title="Mi primera API",
    description="Esta es mi primera API",
    version="0.0.1",
    openapi_tags=[{
        "name": "opiniones",
        "description": "opiniones routes"
    }]
)

app.include_router(data)