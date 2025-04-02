from sqlalchemy import Column, String, Date, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Despesa(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    reg_ans = Column(String(10), nullable=False)
    cd_conta_contabil = Column(String(20), nullable=False)
    descricao = Column(String(255), nullable=False)
    vl_saldo_inicial = Column(Numeric(15, 2), default=0)
    vl_saldo_final = Column(Numeric(15, 2), nullable=False)