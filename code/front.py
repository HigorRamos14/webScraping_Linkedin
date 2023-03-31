import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
import linkedin2


class Tabela(QMainWindow):
    def __init__(self):
        super().__init__()

        linkedin2.webScraping()

        # Dados da tabela
        self.dados = linkedin2.scraping.list_vagas

        # Cria a tabela
        self.tabela = QTableWidget(self)
        self.tabela.setRowCount(len(self.dados))
        self.tabela.setColumnCount(len(self.dados[0]))
        self.tabela.setColumnWidth(0,300)
        self.tabela.setColumnWidth(1,300)
        self.tabela.setColumnWidth(2,300)
        self.tabela.setColumnWidth(3,150)
        self.tabela.setGeometry(0, 100, 1080, 600)
        self.atualiza_tabela()

        # Cria o botão
        botao_atualizar = QPushButton("Atualizar", self)
        botao_atualizar.move(10, 20)
        botao_atualizar.clicked.connect(self.atualiza_tabela)

        botao_atualizar = QPushButton("gerar CSV", self)
        botao_atualizar.move(130, 20)
        botao_atualizar.clicked.connect(linkedin2.scraping.csvArchive)


        # Configura a janela
        self.setGeometry(100, 100, 1080, 720)
        self.setWindowTitle("Tabela")
        self.show()

    def atualiza_tabela(self):
        for i, linha in enumerate(self.dados):
            for j, coluna in enumerate(linha):
                self.tabela.setItem(i, j, QTableWidgetItem(coluna))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabela = Tabela()
    sys.exit(app.exec_())
