import psycopg2

# Configuração do banco de dados
DB_CONFIG = {
    "host": "localhost",
    "database": "agencias",
    "user": "postgres",
    "password": "intuitivecare",
    "port": 5432
}

def execute_sql_file(file_path):
    """
    Executa um arquivo SQL no banco de dados PostgreSQL.
    """
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Ler o arquivo SQL
        with open(file_path, "r") as sql_file:
            sql = sql_file.read()

        # Executar o SQL
        cursor.execute(sql)
        conn.commit()
        print(f"Arquivo {file_path} executado com sucesso!")

    except Exception as e:
        print(f"Erro ao executar o arquivo {file_path}: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Executar os scripts SQL
    execute_sql_file("backend/app/sql/create_tables.sql")
    execute_sql_file("backend/app/sql/importa_dados.sql")