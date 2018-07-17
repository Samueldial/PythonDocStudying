import requests
from BeautifulSoup import BeautifulSoup as Soup

url = "http://agorarn.com.br/cultura/"
req = requests.get (url)
html = Soup (req.content)

articles = html.findAll ('article')
#print len (articles)
for art in articles[1:15]:
    titulo = articles [1].find ('span',{'class':'chapeu'})
    #print titulo.txt
    data = art.find('time').text
    desc = art.find ('h2').text
    print titulo, data, desc
    
    print "-"*10
