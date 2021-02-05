from scraping.scrapy_data_full import get_data_locate, get_data_region, get_data_postcode

class DataInWeb:
    def __init__(self):
        url = 'https://www.postcodearea.co.uk'
        links = get_data_locate(url, self)
        regions = []

        for link in links:
            regions = get_data_region(url+link, self)

            for region in regions:
                print(region)
                file1 = open("links.txt","a") 
                file1.write(url+link+region+"\n") 
                file1.close()



class DataInFile:
    def __init__(self, name_file):

        with open(name_file, 'r') as file:
            self.links = file.read().split()

        for link in self.links:
            postcodes = get_data_postcode(link, self)

            for postcode in postcodes:
                # print(postcode)
                file1 = open("postcodes.txt","a") 
                file1.write(postcode+"\n") 
                file1.close()


if __name__ == '__main__':
    DataInWeb()
    DataInFile( 'links.txt' )
