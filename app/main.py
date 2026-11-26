from fastapi import FastAPI
from app.database import engine, Base
from app.models.tutor import Tutor
from app.models.pet import Pet
from app.routers import tutores
from app.routers import pets

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Hotel Pet",
    description="API para gerenciamento de tutores e pets",
    version="1.0.0"
)

app.include_router(tutores.router)

app.include_router(pets.router)


@app.get("/")
def inicio():
    return {"mensagem": "API Hotel Pet funcionando!"}