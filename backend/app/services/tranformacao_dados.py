import pdfplumber
import pandas as pd
import zipfile
import os
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Caminhos dos arquivos
pdf_path = "./assets/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf" 
csv_path = "./assets/tabela.csv"
xlsx_path = "./assets/tabela.xlsx"
zip_path = "./assets/Teste_Artur.zip" 

#Substitui as legendas OD e AMB por seus respectivos significados
legenda = {
    "OD": "Procedimentos Odontológicos",
    "AMB": "Procedimentos Ambulatoriais"
}

# Função para extrair tabelas de um PDF usando pdfplumber
def extract_table_from_pdf(pdf_path):
    data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # Remove linhas vazias e espaços extras
                    if row and any(row):
                        data.append([cell.strip() if cell else "" for cell in row])
    
    return data


data = extract_table_from_pdf(pdf_path)

# Dataframe
df = pd.DataFrame(data)

# Ajustando cabeçalhos dinamicamente
num_colunas = df.shape[1]  
df.columns = [f"Coluna_{i}" for i in range(num_colunas)] 

# Tentativa de identificar cabeçalhos automaticamente
possiveis_cabecalhos = df.iloc[0].tolist()
if "Código" in possiveis_cabecalhos or "Descrição" in possiveis_cabecalhos:
    df.columns = possiveis_cabecalhos 
    df = df[1:] 

# Substitui abreviações OD e AMB
df.replace(legenda, inplace=True)

# Remove colunas vazias e linhas duplicadas
df.dropna(how="all", inplace=True)
df.drop_duplicates(inplace=True)

# Salvar no formato Excel com autoajuste de largura das colunas
wb = Workbook()
ws = wb.active

# Preenchendo as células do Excel com os dados do DataFrame
for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
    for c_idx, value in enumerate(row, 1):
        ws.cell(row=r_idx, column=c_idx, value=value)

# Ajuste automático de largura das colunas no Excel
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Obter a letra da coluna
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except Exception as e:
            print (f"Erro ao calcular o comprimento da célula: {e}")
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

# Salvar o arquivo Excel
wb.save(xlsx_path)

# Agora, salvar o DataFrame como CSV
df.to_csv(csv_path, index=False, encoding='utf-8-sig', sep=';', lineterminator='\n')

# Compactando os arquivos CSV e Excel
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))
    zipf.write(xlsx_path, os.path.basename(xlsx_path))

print(f"Arquivo compactado salvo como {zip_path}")
