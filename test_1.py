from lxml import html
import requests
from bs4 import BeautifulSoup

for i in range(1,2,1):
    url = 'http://marinamercante.gob.hn/consultas/buques.php?nombre=%25&Submit=Buscar&page=%'+str(i)
    response = requests.get(url)
    page = response
    tree = html.fromstring(page.content)
    #print tree

    # This will create a list of buyers:
    buyers = tree.xpath('//tr//td[@bgcolor="#E6E1D5"]/text_content()')
    print buyers

