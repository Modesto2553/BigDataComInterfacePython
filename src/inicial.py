import tkinter as tk
from tkinter import filedialog

class Frameinicio(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.principal = master
        self.width = 500
        self.height = 500
        self.canvas = tk.Canvas(bg="black", width=500, height=500, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        self.background_img = tk.PhotoImage(file=f"./imagem/fundo.png")
        self.background = self.canvas.create_image(250, 250, image=self.background_img)

        self.img = tk.PhotoImage(file=f"./imagem/seleciona.png")
        self.btn = tk.Button(image=self.img, borderwidth=0, highlightthickness=0,
                                        command=self.selecionar_arquivo,
                                        relief="flat", anchor="nw")
        self.btn.place(x=180.5, y=230, width=139, height=40)

    def selecionar_arquivo(self):
        # Abre a janela de seleção de arquivo e retorna o caminho do arquivo selecionado
        self.caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
        )
        # Exibe o caminho do arquivo selecionado na label
        self.caminho = tk.Label(text=self.caminho_arquivo, font=("Arial", 11))
        self.caminho.place(x=180.5, y=280)

        self.caminho.after(100, self.obter_largura)

        self.img_seguir = tk.PhotoImage(file=f"./imagem/continuar.png")
        self.btn_seguir = tk.Button(image=self.img_seguir, borderwidth=0, highlightthickness=0,
                             command=self.principal.main,
                             relief="flat", anchor="nw")
        self.btn_seguir.place(x=109, y=400, width=282, height=40)

    def obter_largura(self):
        # Obter a largura do botão após a renderização
        self.largura = self.caminho.winfo_width()
        self.novo_x = 250 - (self.largura / 2)

        # Atualizar a posição x da label para centralizá-la
        self.caminho.place(x=self.novo_x)


