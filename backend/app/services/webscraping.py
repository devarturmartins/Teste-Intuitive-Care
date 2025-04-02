import requests
from bs4 import BeautifulSoup
import os
import zipfile
from tkinter import Tk
from tkinter.filedialog import askdirectory

URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

ZIP_FILE_NAME = 'anexos.zip'


def valida_requisicao(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print(f"Falha na requisição: {response.status_code}")
        return None


def corrige_link(href):
    if href.startswith('http'):
        return href
    else:
        return f'https://www.gov.br{href}'


def baixa_pdf(pdf_url, save_dir):
    pdf_response = requests.get(pdf_url)
    if pdf_response.status_code == 200:
        file_name = os.path.join(save_dir, pdf_url.split('/')[-1])
        with open(file_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print(f"Download concluído: {file_name}")
        return file_name
    else:
        print(f"Falha ao baixar o arquivo: {pdf_url}")
        return None


def busca_pdfs(url, save_dir):
    response = valida_requisicao(url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        arquivos_baixados = []

        anexo_i_tag = soup.find('a', string='Anexo I.')
        if anexo_i_tag:
            href = anexo_i_tag['href']
            pdf_url = corrige_link(href)
            caminho_pdf = baixa_pdf(pdf_url, save_dir)
            if caminho_pdf:
                arquivos_baixados.append(caminho_pdf)

        anexo_ii_tag = soup.find('a', string='Anexo II.')
        if anexo_ii_tag:
            href = anexo_ii_tag['href']
            pdf_url = corrige_link(href)
            caminho_pdf = baixa_pdf(pdf_url, save_dir)
            if caminho_pdf:
                arquivos_baixados.append(caminho_pdf)

        return arquivos_baixados
    return []


def compacta_arquivos(arquivos, zip_file_name, save_dir):

    zip_path = os.path.join(save_dir, zip_file_name)
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for arquivo in arquivos:
                zipf.write(arquivo, os.path.basename(arquivo))
        print(f"Arquivos compactados em: {zip_path}")
    except Exception as e:
        print(f"Erro ao compactar os arquivos: {e}")

def main():
    Tk().withdraw()
    save_dir = askdirectory(title="Selecione o diretório para salvar os arquivos")
    if not save_dir:
        print("Nenhum diretório selecionado. Encerrando o programa.")
        return

    print("Iniciando o processo...")
    arquivos_baixados = busca_pdfs(URL, save_dir)
    if arquivos_baixados:
        compacta_arquivos(arquivos_baixados, ZIP_FILE_NAME, save_dir)
    else:
        print("Nenhum arquivo foi baixado.")


if __name__ == '__main__':
    main()