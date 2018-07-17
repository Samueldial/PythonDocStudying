import requests

url = "http://10.190.6.52/ifrn/minicurso/captcha.php"

req = requests.get(url)
cookies = req.cookies
#baixei a imagem
f = open('imagem.png','wb')
f.write(req.content)
f.close()

url = "http://10.190.6.52/ifrn/minicurso/valida.php"


#ler o codigo automaticamente
from PIL import Image
import pytesseract

img = Image.open('imagem.png')
img = img.convert("RGBA")
pixdata = img.load()
#tirar as cores e tracos
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][0] > 63:
            pixdata[x, y] = (255,255,255,255)
#duplicar o tamanho
width = img.size[0] * 2
height = img.size[1] * 2
img = img.resize((width,height), Image.ANTIALIAS)

img.save("imagem-nova.png")

codigo = pytesseract.image_to_string(img).replace(" ","")
print codigo, "<<"

#codigo = raw_input("Digite o captcha")
dados = {'captcha':codigo}

req = requests.post(url,data=dados,cookies=cookies)
print req.content



