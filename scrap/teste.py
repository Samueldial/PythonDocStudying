import requests
from BeautifulSoup import BeautifulSoup as Soup

url = "http://www.tjrn.jus.br/pje"
req = requests.get (url)

html = Soup (req.content)

#for link in html.findAll ("a"):
    #print link.text

link = html.find ("a", text="Requisitos")
print link.parent.get ('href')



