import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class Framedirecionar(tk.Frame):
    def __init__(self, master, dados):
        super().__init__(master)
        self.dados = dados
        self.width = 1366
        self.height = 768
        self.canvas = tk.Canvas(bg="black", width=1366, height=768, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        self.background_img = tk.PhotoImage(file=f"./imagem/direcionar.png")
        self.background = self.canvas.create_image(683, 384, image=self.background_img)

        self.img = tk.PhotoImage(file=f"./imagem/venda_mes.png")
        self.btn_venda_mes = tk.Button(image=self.img, borderwidth=0, highlightthickness=0,
                             command=self.criar_grafico,
                             relief="flat", anchor="nw", text='Vendas Por Mês', font=('Arial', 20))
        self.btn_venda_mes.place(x=58, y=270, width=175, height=40)

        self.img1 = tk.PhotoImage(file=f"./imagem/venda_dia.png")
        self.btn_venda_produto = tk.Button(image=self.img1, borderwidth=0, highlightthickness=0,
                                       command=self.criar_grafico_dia,
                                       relief="flat", anchor="nw", text='Vendas Por Mês', font=('Arial', 20))
        self.btn_venda_produto.place(x=58, y=320, width=175, height=40)

        self.img2 = tk.PhotoImage(file=f"./imagem/venda_produto.png")
        self.btn_crescimento = tk.Button(image=self.img2, borderwidth=0, highlightthickness=0,
                                       command=self.criar_grafico_por_produto,
                                       relief="flat", anchor="nw", text='Vendas Por Mês', font=('Arial', 20))
        self.btn_crescimento.place(x=58, y=370, width=175, height=40)




    def criar_grafico(self):
        # Sofia
            self.df = pd.DataFrame.from_dict(self.dados)
            # Criar figura do Matplotlib
            self.soma_por_numero = self.df.groupby('Mês')['Total'].sum()

            # Luciano
            self.fig, self.ax = plt.subplots()
            self.ax.bar(self.soma_por_numero.index, self.soma_por_numero.values)
            self.ax.set_xlabel('Mês')
            self.ax.set_ylabel('Total de Vendas por Mês')
            self.ax.set_title('Vendas por Mês')

            # Criar um objeto FigureCanvasTkAgg passando a figura Matplotlib
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)  # 'root' é o widget principal do tkinter
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x=250, y=130, width=1000, height=600)

    def criar_grafico_dia(self):
        self.df = pd.DataFrame.from_dict(self.dados)
        # Criar figura do Matplotlib
        self.soma_por_numero = self.df.groupby('Data')['Total'].sum()

        # Luciano
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.soma_por_numero)
        self.ax.set_xlabel('Dia')
        self.ax.set_ylabel('Total de Vendas por dia')
        self.ax.grid(True)
        self.ax.set_title('Vendas por dia')

        # Criar um objeto FigureCanvasTkAgg passando a figura Matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)  # 'root' é o widget principal do tkinter
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=250, y=130, width=1000, height=600)

    def criar_grafico_por_produto(self):
        self.df = pd.DataFrame.from_dict(self.dados)
        # Criar figura do Matplotlib
        self.soma_por_numero = self.df.groupby('Produto')['Quantidade'].sum()
        self.soma_por_numero = pd.concat([self.soma_por_numero.head(5), self.soma_por_numero.tail(5)])

        self.fig, self.ax = plt.subplots()
        self.ax.pie(self.soma_por_numero.values, labels=self.soma_por_numero.index, autopct='%.2f')
        self.ax.set_title('Distribuição de Categorias de Produtos em Porcentagem')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)  # 'root' é o widget principal do tkinter
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=250, y=130, width=1000, height=600)


