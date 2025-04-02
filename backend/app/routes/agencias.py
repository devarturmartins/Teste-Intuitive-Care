from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.agencias import Agencia

router = APIRouter()

@router.get("/buscar")
def buscar_operadoras(
    termo: str = Query(..., description="Termo de busca textual"),
    db: Session = Depends(get_db)
):
    """
    Rota para buscar operadoras com base em um termo textual.
    """
    resultados = db.query(Agencia).filter(
        Agencia.razao_social.ilike(f"%{termo}%") |
        Agencia.nome_fantasia.ilike(f"%{termo}%") |
        Agencia.modalidade.ilike(f"%{termo}%")
    ).all()
    return resultados