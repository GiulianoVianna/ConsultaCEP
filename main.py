import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt5.uic import loadUi
import requests

class ConsultaCEP(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega a interface do usuário a partir do arquivo .ui
        loadUi('cep.ui', self)

        # Conecta o sinal de clique do botão à função para mostrar informações da cidade
        self.search_button.clicked.connect(self.mostrar_informacoes_cidade)

        # Define o tamanho fixo da janela
        self.setFixedSize(400, 177)

    # Consulta a API do ViaCEP para obter informações do CEP fornecido
    def obter_informacoes_cep(self, cep):
        
        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return None
        
    # Obtém o CEP digitado pelo usuário
    def mostrar_informacoes_cidade(self):
        
        cep = self.cep_input.text()

        # Obtém as informações do CEP
        informacoes_cep = self.obter_informacoes_cep(cep)

        # Atualiza o texto do rótulo (label) com as informações da cidade
        if informacoes_cep:
            self.city_info_label.setText(f"Cidade: {informacoes_cep['localidade']} - {informacoes_cep['uf']}\nBairro: {informacoes_cep['bairro']}\nLogradouro: {informacoes_cep['logradouro']}")
        else:
            self.city_info_label.setText('CEP não encontrado')

# Inicializa a aplicação
app = QApplication(sys.argv)

# Cria e exibe a janela principal
janela_consulta_cep = ConsultaCEP()
janela_consulta_cep.show()

# Executa o loop de eventos da aplicação
sys.exit(app.exec_())
