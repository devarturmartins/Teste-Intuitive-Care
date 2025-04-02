from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Agencia(Base):
    __tablename__ = "agencias"

    registro_ans = Column(String(10))
    cnpj = Column(String(14), nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255))
    modalidade = Column(String(100))
    logradouro = Column(String(255))
    numero = Column(String(20))
    complemento = Column(String(255))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(String(2))
    cep = Column(String(8))
    ddd = Column(String(2))
    telefone = Column(String(20))
    fax = Column(String(20))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(255))
    regiao_comercializacao = Column(String(100))
    data_registro_ans = Column(Date)
