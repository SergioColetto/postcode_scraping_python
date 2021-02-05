from scraping.funtion import html_convert_python

def get_data_page_locate(url):

    soup = html_convert_python( url )
    data = []

    for row in soup.find("ul", {"id": "postcode-list"}).find_all("li"):

        url = row.find('a').attrs['href']
        data.append(url)

    return data


def get_data_page_region(url):

    soup = html_convert_python( url )
    data = []

    for row in soup.find_all("div", {"class": "col-md-3 col-xs-4"}):

        url = row.a.get('href')
        print(url)
        data.append(url)

    return data


def get_data_page_postcode(url):

    soup = html_convert_python( url )
    data = []

    for row in soup.find_all("div", {"class": "col-md-3 col-xs-12"}):

        url = row.a.string
        print(url)
        data.append(url)

    return data
