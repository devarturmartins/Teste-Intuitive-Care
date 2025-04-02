# Usar uma imagem base do Python
FROM python:3.10-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt da raiz do projeto para o contêiner
COPY ../../requirements.txt /app/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o restante do código do backend
COPY ./backend/app /app

# Expor a porta do backend
EXPOSE 8000

# Comando padrão para o contêiner

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "python", "app/services/executa_sql.py"]