# API WWW em python
# urlopen faz uma requisição ao servidor 
# retornando o conteudo escrito html do site

from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('http://www.uol.com')
# print(html)

# html parser faz uma varredura nas tags do HTML
# apenas chamando HTMLParser não faz nada
# tem que especificar qual tag quer que faça a varredura

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

parser = MyParser()
# parser.feed(html)

# irá verificar quantos polos existem no site da univesp
# observação, é ideal verificar qual elemento esta na busca
# verificando o codigo fonte e suas respectivas tags
# refernte a informação em que busca

from html.parser import HTMLParser
from urllib.request import urlopen, Request

class MyParser(HTMLParser): 
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_polos = 0

    def handle_starttag(self, tag, attrs): # especifica oque quero que busque
        if tag == 'p':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'item-polos':
                    self.n_polos += 1
    def num_polos(self):
        return self.n_polos
    
def getSource(url): # simula um navegador para sites não bloquearem por ser um acesso anonimo
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0Safari/537.3'}
    reg_url = "https:XXXXOOOO"
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return html.decode()

html = getSource('https://univesp.br/cursos/engenharia-de-computacao') # site que sera feito a busca
parser = MyParser()
parser.feed(html)
parser.num_polos()