# TESTE DE WEB SCRAPING

import requests
from bs4 import BeautifulSoup
import os
import zipfile
from tkinter import Tk
from tkinter.filedialog import askdirectory

# URL do site
URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

# Nome do arquivo ZIP final
ZIP_FILE_NAME = 'anexos.zip'


def valida_requisicao(url):
    """
    Verifica se a requisição ao site foi bem-sucedida.
    :param url: URL do site
    :return: Objeto response se bem-sucedido, None caso contrário
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print(f"Falha na requisição: {response.status_code}")
        return None


def corrige_link(href):
    """
    Corrige links relativos para links absolutos.
    :param href: Link encontrado na página
    :return: Link absoluto
    """
    if href.startswith('http'):
        return href
    else:
        return f'https://www.gov.br{href}'


def baixa_pdf(pdf_url, save_dir):
    """
    Faz o download de um arquivo PDF e salva no diretório especificado.
    :param pdf_url: URL do arquivo PDF
    :param save_dir: Diretório onde o arquivo será salvo
    :return: Caminho completo do arquivo salvo
    """
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
    """
    Busca os links dos PDFs Anexo I e Anexo II na página e faz o download.
    :param url: URL do site
    :param save_dir: Diretório onde os arquivos serão salvos
    :return: Lista de caminhos dos arquivos baixados
    """
    response = valida_requisicao(url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        arquivos_baixados = []

        # Busca o link do Anexo I
        anexo_i_tag = soup.find('a', string='Anexo I.')
        if anexo_i_tag:
            href = anexo_i_tag['href']
            pdf_url = corrige_link(href)
            caminho_pdf = baixa_pdf(pdf_url, save_dir)
            if caminho_pdf:
                arquivos_baixados.append(caminho_pdf)

        # Busca o link do Anexo II
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
    """
    Compacta os arquivos em um único arquivo ZIP.
    :param arquivos: Lista de caminhos dos arquivos a serem compactados
    :param zip_file_name: Nome do arquivo ZIP final
    :param save_dir: Diretório onde o arquivo ZIP será salvo
    """
   # Caminho completo do arquivo ZIP
    zip_path = os.path.join(save_dir, zip_file_name)
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for arquivo in arquivos:
                # Adiciona o arquivo ao ZIP com o nome base (sem o caminho completo)
                zipf.write(arquivo, os.path.basename(arquivo))
        print(f"Arquivos compactados em: {zip_path}")
    except Exception as e:
        print(f"Erro ao compactar os arquivos: {e}")

def main():
    """
    Função principal que executa o processo completo:
    1. Solicita o diretório de download ao usuário.
    2. Busca e baixa os PDFs Anexo I e Anexo II.
    3. Compacta os arquivos baixados em um único arquivo ZIP.
    """
    # Solicita o diretório de download ao usuário
    Tk().withdraw()  # Oculta a janela principal do Tkinter
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