import requests
from bs4 import BeautifulSoup

def html_convert_python(url):
    
    req_get = requests.get(url)
    return BeautifulSoup(req_get.content, 'html.parser')
