import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "agencias",
    "user": "postgres",
    "password": "intuitivecare",
    "port": 5432
}

def execute_sql_file(file_path):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        with open(file_path, "r") as sql_file:
            sql = sql_file.read()

        cursor.execute(sql)
        conn.commit()
        print(f"Arquivo {file_path} executado com sucesso!")

    except Exception as e:
        print(f"Erro ao executar o arquivo {file_path}: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    execute_sql_file("./backend/app/sql/create_table.sql")
    execute_sql_file("./backend/app/sql/importa_dados.sql")