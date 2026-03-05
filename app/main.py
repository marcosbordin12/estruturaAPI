from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Estrutura API",
    description="API exemplo para verificar estrutura",
    version="1.0"
)

app.include_router(router)