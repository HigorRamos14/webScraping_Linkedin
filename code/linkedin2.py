import requests
from bs4 import BeautifulSoup
import pandas as pd

class webScraping():
    def __init__(self):
        headers = {'user-agent': 'Mozilla/5.0'}

        self.resposta = requests.get('https://www.linkedin.com/jobs/search?keywords=Marketing&location=Brasil&locationId=&geoId=106057199&f_TPR=&f_JT=F&f_E=1&position=1&pageNum=0',
                                headers = headers)

        self.htmlLinkedinBruto = self.resposta.text
        self.htmlLinkedin_organized = BeautifulSoup(self.htmlLinkedinBruto, 'html.parser')

        self.class_vagas = self.htmlLinkedin_organized.find_all('div', {'class' : 'base-search-card__info'})
        self.class_metadata = self.htmlLinkedin_organized.find_all('div', {'class' : 'base-search-card__metadata'})

        self.list_vagas = []
        self.cont = 0

        while self.cont < len(self.class_vagas):
            self.nomeDaVaga = self.class_vagas[self.cont].find('h3').text
            self.nomeDaEmpresa = self.class_vagas[self.cont].find('h4').text
            
            self.localDaEmpresa = self.class_metadata[self.cont].find('span').text
            self.tempoDePostagem = self.class_metadata[self.cont].find('time').text

            self.list_vagas.append((self.nomeDaVaga.strip(), self.nomeDaEmpresa.strip(), self.localDaEmpresa.strip(), self.tempoDePostagem.strip()))

            self.cont = self.cont + 1
        
    def csvArchive(self):
        self.final_list = self.list_vagas

        self.info = pd.DataFrame(self.final_list, columns=['vagas', 'empresas', 'local', 'data de postagem'])
        self.info.to_csv('linkedin2.csv')

scraping = webScraping()
