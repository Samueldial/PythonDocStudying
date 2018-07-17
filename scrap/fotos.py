import requests
from BeautifulSoup import BeautifulSoup as Soup

url = "http://www.canstockphoto.com/"
url += "stock-photo-images/praia.html"

req = requests.get (url)

html = Soup (req.content)

imagens = html.findAll ('img')
for img in imagens:
    link = img.get ('src')
    req = requests.get (link)
    nome = link.split("/")[-1]
    print nome
    f = open ('img/'+nome,'w')
    f.write (req.content)
    f.close ()
