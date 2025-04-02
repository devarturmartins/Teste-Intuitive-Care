from fastapi import FastAPI
from app.routes import agencias

# Inicializa o FastAPI
app = FastAPI()

# Inclui as rotas
app.include_router(agencias.router, prefix="/api/agencias", tags=["Agencias"])

@app.get("/")
def root():
    return {"message": "API está funcionando!"}