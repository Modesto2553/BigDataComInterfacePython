import PyPDF2 as pyf
from datetime import datetime

class dados():
    def __init__(self, caminho):
        self.caminho = caminho
        self.arquivo = pyf.PdfReader(f'{self.caminho}')

        self.texto_pdf = ''

        for i, self.pagina in enumerate(self.arquivo.pages):
            # Pega de cada página
            self.texto_pagina = self.pagina.extract_text()

            # Exclui o começo e o fim do pdf que não irá utilizar
            self.texto_pagina = self.texto_pagina[295:]
            self.texto_pagina = self.texto_pagina[:-48]

            # Coloca tudo em uma variavel
            self.texto_pdf += f'{self.texto_pagina}\n'

        # Define as variaveis
        self.texto_referencia = "REFERÊNCIA TIPO"
        self.n_venda = []
        self.referencia = []
        self.qtd = []
        self.total = []
        self.produtos = []
        self.tipo = []
        self.data = []

        # Conta quantas vezes o texto referencia aparece
        self.quantidade = self.texto_pdf.lower().count(self.texto_referencia.lower())
        self.posicao_final = 0
        self.texto_analisar = self.texto_pdf
        for i in range(self.quantidade):
            # Seleciona a parte do texto a partir da posi
            self.texto_analisar = self.texto_analisar[self.posicao_final:]

            # Pega em qual posição cada referencia está
            self.posicao_inicial = self.texto_analisar.find(self.texto_referencia) + 15
            self.posicao_final = self.texto_analisar.find('TOTAL', self.posicao_inicial + 1)

            self.posicao_data = self.posicao_inicial
            self.data_texto = self.texto_analisar[self.posicao_data - 26:self.posicao_data - 15]

            self.texto_final = self.texto_analisar[self.posicao_inicial:self.posicao_final]
            # Separa o texto
            self.texto_final = self.texto_final.split('\n')
            self.texto_final = list(filter(None, self.texto_final))

            for self.texto in self.texto_final:
                self.texto = self.texto.split(' ')
                self.texto = list(filter(None, self.texto))

                self.n_venda.append(self.texto[0])
                self.referencia.append(self.texto[1])
                self.qtd.append(int(self.texto[2]))
                self.total.append(self.texto[3])
                self.produtos.append(self.texto[4:-1])
                self.tipo.append(self.texto[-1:])
                self.data.append(str(self.data_texto))


        self.list_produtos = []
        for produto in self.produtos:
            self.texto = ''
            for n in produto:
                self.texto += f' {n}'
            self.list_produtos.append(self.texto)

        self.mes = []
        self.dia = []
        self.meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        for i, d in enumerate(self.data):
            self.data[i] = d.replace('\n', '')
            self.data[i] = datetime.strptime(self.data[i], "%d/%m/%Y")
            self.data[i] = self.data[i].date()
            self.dia.append(int(self.data[i].day))
            self.mes.append(self.meses[int(self.data[i].month) - 1])

        for i, self.t in enumerate(self.tipo):
            self.tipo[i] = self.t[0]

        for i, t in enumerate(self.total):
            self.total[i] = t.replace(',', '.')
            self.total[i] = float(self.total[i])

        self.dados = {
            'N Venda': self.n_venda,
            'Tipo': self.tipo,
            'Referencia': self.referencia,
            'Produto': self.list_produtos,
            'Quantidade': self.qtd,
            'Total': self.total,
            'Data': self.data,
            'Dia': self.dia,
            'Mês' : self.mes
        }

    def retornar(self, app):
        return self.dados


