import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0'}

resposta = requests.get('https://www.linkedin.com/jobs/search?keywords=Marketing&location=Brasil&locationId=&geoId=106057199&f_TPR=&f_JT=F&f_E=1&position=1&pageNum=0',
                        headers = headers)

htmlLinkedinBruto = resposta.text
htmlLinkedin_organized = BeautifulSoup(htmlLinkedinBruto, 'html.parser')

class_vagas = htmlLinkedin_organized.find_all('div', {'class' : 'base-search-card__info'})
class_metadata = htmlLinkedin_organized.find_all('div', {'class' : 'base-search-card__metadata'})

list_vagas = []
cont = 0

while cont < len(class_vagas):
    nomeDaVaga = class_vagas[cont].find('h3').text
    nomeDaEmpresa = class_vagas[cont].find('h4').text
    
    localDaEmpresa = class_metadata[cont].find('span').text
    tempoDePostagem = class_metadata[cont].find('time').text

    list_vagas.append((nomeDaVaga.strip(), nomeDaEmpresa.strip(), localDaEmpresa.strip(), tempoDePostagem.strip()))

    cont = cont + 1

info = pd.DataFrame(list_vagas, columns=['vagas', 'empresas', 'local', 'data de postagem'])
info.to_csv('linkedin2.csv')