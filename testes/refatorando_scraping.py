import requests
from bs4 import BeautifulSoup
import pandas as pd


# Função que busca as pastas e arquivos encontrado com a página especificada
def get_navegation(obj_soup, page_main):
    # lista para os dicionarios recebidos
    data = []
    # como a classe das subpastas são diferentes é preciso criar uma função para diferenciar
    # a primeira request na página principal das demais
    if page_main:
        # caso a page_main seja True passa o conteudo referente a classe da pagina principal
        grid = 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block'
    else:
        # Recebe a classe de subpastas
        grid = 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-block'

    # Primeiro pesquisamos a classe reponsavel por armazenar os arquivos que procuramos
    # e extraimos uma lista com apenas os que contem a tag role = 'row', após a priemira linha que nao precisamos

    for row in obj_soup.find(class_=grid).find_all(role="row")[1:]:
        try:
            # Pega o tipo de arquivo (Pasta, Arquivo, Symlink File)
            type_file = row.svg['aria-label']

            if type_file != 'Directory':
                type_file = 'File'
        except:
            type_file = 'File'
        # a url armazenada no href
        url = row.find('a').attrs['href']

        # Nome do arquivo
        try:
            name = row.find('a').attrs['title']
        except KeyError:
            name = 'others'

        extension = 'Directory'

        if type_file != 'Directory':
            extension = name.split('.')[-1]

            # junta os dados em um dicionario e adiciona dentro de uma lista
        data.append({'type_file': type_file, 'url': url, 'name': name, 'extension': extension})

    return data


# Função converte uma o html de uma url para obj python do bs4
def html_convert_python(url):
    # print(f'Convertendo url {url} para bs4')
    # Faz uma requisição trasendo o html
    req_get = requests.get(url)
    # A Beautiful Soup analisa o documento usando o melhor analisador disponível.
    # Ele usará um analisador HTML
    return BeautifulSoup(req_get.content, 'html.parser')  # retornando o obj


def gera_dados_repositorio(nome_repositorio):
    urls_directories = [nome_repositorio]
    data_full = []
    page_main = True
    while len(urls_directories) > 0:
        subdirectories = []
        for url_directory in urls_directories:
            # print(url_directory)
            collected_data = get_navegation(
                html_convert_python('https://github.com' + url_directory.replace('https://github.com', '')),
                page_main)

            for data in collected_data:
                data_full.append(data)
                if data['type_file'] == 'Directory':
                    subdirectories.append(data['url'])

        page_main = False
        urls_directories = subdirectories

    for item in data_full:
        print(item)

    # print(data_full)
    df = pd.DataFrame(data_full)
    return df


repos = ['Erickson-lopes-dev/Python_BeautifulSoup_V4.9.2',
         # 'Erickson-lopes-dev/Python_BeautifulSoup_V4.9.2',
         # 'frontpressorg/frontpress',
         # 'SambitAcharya/Mini-Projects',
         # 'jenkinsci/docker',
         # 'docker/compose'
         ]

for repo in repos:
    url_repo = 'https://github.com/' + repo
    # print(url_repo)
    gera_dados_repositorio(url_repo)
    print()
    # get_navegation(html_convert_python(url_repo), True)
    # break
