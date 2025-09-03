import tkinter as tk
from inicial import Frameinicio
from direcionar import Framedirecionar
from teste import dados

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tela_inicial()


    def tela_inicial(self):
        self.frame1 = Frameinicio(self)
        self.frame1.grid(row=0, column=0)

    def main(self):
        self.caminho = self.frame1.caminho_arquivo
        self.dados = dados(self.caminho).retornar(self)
        self.frame1.destroy()
        self.frame2 = Framedirecionar(self, self.dados)
        self.frame2.grid(row=0, column=0)




if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
