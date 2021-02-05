from scraping.scrapy_tree import get_data_page_locate, get_data_page_region, get_data_page_postcode
from tqdm import tqdm

def get_data_locate(url, self):

    print('\n')
    print(f"Buscando dados em '{url}'")
    data = get_data_page_locate( url )
    return data

def get_data_region(url, self):

    print('\n')
    print(f"Buscando dados em '{url}'")
    data = get_data_page_region( url )
    return data

def get_data_postcode(url, self):

    print('\n')
    print(f"Buscando dados em '{url}'")
    data = get_data_page_postcode( url )
    return data
