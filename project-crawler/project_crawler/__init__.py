import requests
import lxml
from bs4 import BeautifulSoup

# Get the html content of the page
def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    f = requests.get(url, headers=headers) # make http request to the url
    soup = BeautifulSoup(f.content, 'lxml') # parse the html content
    return soup

# Get the urls of the page
def get_urls(list, begin_url):
    type_list = []

    for anchor in list:
        urls = begin_url + anchor['href']
        type_list.append(urls)
    
    return type_list


# Page 1
url1 = 'https://www.epn.edu.ec/oferta-academica/grado/ingenieria-tecnologia'
soup = get_soup(url1)
elements = soup.find('div',{'class':'options'}).find_all('a')
careers_url = get_urls(elements, url1)
print("\n***RESULTS OF PAGE 1***")
for i in range(0, len(careers_url)):
    print("Link: " + careers_url[i])
    print("Career: " + elements[i].text)


# Page 2
url2 = 'https://es.wikipedia.org/wiki/Salud'
soup = get_soup(url2)
index_page = soup.find_all('span', {'class':'mw-headline'})
print("***RESULTS OF PAGE 2***")
print("Index:")
for element in index_page:
    print(element.text)


# Page 3
url3 = 'https://www.sensacine.com/peliculas/mejores-peliculas'
url3_aux = 'https://www.sensacine.com'
soup = get_soup(url3)
elements = soup.find_all('a', {'class':'meta-title-link'})
movies_url = get_urls(elements, url3_aux)
print("\n***RESULTS OF PAGE 3***")
for i in range(0, len(movies_url)):
    print("Link: " + movies_url[i])
    print("Movie: " + elements[i].text)

print('\n')