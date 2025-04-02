from fastapi import FastAPI
from routes import agencias
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(agencias.router, prefix="/api/agencias", tags=["Agencias"])

@app.get("/")
def root():
    return {"message": "API está funcionando!"}
