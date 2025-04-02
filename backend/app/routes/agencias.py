from fastapi import APIRouter, Query
import pandas as pd 
from typing import List
import logging

router = APIRouter()

CSV_PATH = '/assets/Relatorio_cadop.csv'

try:
    df = pd.read_csv(CSV_PATH, delimiter=";", encoding="utf-8")
    logging.info(f"CSV carregado com sucesso. Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
except Exception as e:
    logging.error(f"Erro ao carregar o CSV: {e}")
    df = pd.DataFrame()


try:
    df = pd.read_csv(CSV_PATH, delimiter=";", encoding="utf-8")
except FileNotFoundError:
    raise Exception(f"Arquivo CSV não encontrado no caminho: {CSV_PATH}")

@router.get("/agencias/", response_model=List[dict])
def search_agencias(term: str = Query("", description="Termo de busca")):
    """
    Busca agências no CSV com base no termo fornecido.
    O termo será buscado em todas as colunas relevantes.
    """
    mask = False
    for col in df.select_dtypes(include=["object"]).columns:
        mask |= df[col].str.contains(term, case=False, na=False)

    resultados = df[mask]

    return resultados.to_dict(orient="records")
