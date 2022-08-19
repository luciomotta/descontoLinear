from tkinter import *


# //////////////////////// criando janela \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Criando um container p\ o widgets (Sua hierar que de saber quem e o PAI)
'''
class Application:
    #Crio o 1º widget e fez o botão SAIR
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()

#P/ criar o evento de clique no botão
    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
'''
    # verificar senha
class Application:



    def calculo(self, master=None):
        valor = self.nome2.get()
        percent = self.senha2.get()

        valor1 = int(valor)
        percent1 = int(percent)

        venda = valor1 / 100
        result = percent1 / venda
        self.mensagem["text"] = (result,"%")


    def calc(self, master=None):

        self.titulo.forget()
        self.nomeLabel.forget()
        self.nome.forget()
        self.senhaLabel.forget()
        self.senha.forget()
        self.autenticar.forget()

        self.fontePadrao1 = ("Arial", "10")
        self.primeiroContainer1 = Frame(master)
        self.primeiroContainer1["pady"] = 10
        self.primeiroContainer1.pack()

        self.segundoContainer1 = Frame(master)
        self.segundoContainer1["padx"] = 20
        self.segundoContainer1.pack()

        self.terceiroContainer1 = Frame(master)
        self.terceiroContainer1["padx"] = 20
        self.terceiroContainer1.pack()

        self.quartoContainer1 = Frame(master)
        self.quartoContainer1["pady"] = 20
        self.quartoContainer1.pack()

        self.titulo1 = Label(self.primeiroContainer, text="Sistema ALIBABA")
        self.titulo1["font"] = ("Arial", "10", "bold")
        self.titulo1.pack()

        self.nomeLabel1 = Label(self.segundoContainer, text="Valor da Venda R$:", font=self.fontePadrao)
        self.nomeLabel1.pack(side=LEFT)

        self.nome2 = Entry(self.segundoContainer)
        self.nome2["width"] = 30
        self.nome2["font"] = self.fontePadrao
        self.nome2.pack(side=LEFT)

        self.senhaLabel1 = Label(self.terceiroContainer, text="Valor de descontoR$", font=self.fontePadrao)
        self.senhaLabel1.pack(side=LEFT)

        self.senha2 = Entry(self.terceiroContainer)
        self.senha2["width"] = 30
        self.senha2["font"] = self.fontePadrao
        self.senha2.pack(side=LEFT)

        self.autenticar1 = Button(self.quartoContainer)
        self.autenticar1["text"] = "Calcular"
        self.autenticar1["font"] = ("Calibri", "8")
        self.autenticar1["width"] = 12
        self.autenticar1["command"] = self.calculo
        self.autenticar1.pack()


        self.mensagem1 = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem1.pack()


    # Método verificar senha
    def verificaSenha(self, master=None):
        usuario = self.nome.get()
        senha = self.senha.get()
        arq = open('registradosSenhas.txt')  # abrindo no modo de leitura
        arq1 = open('registradosNome.txt')  # abrindo no modo de leitura
        registrados = arq.readlines()
        registrados1 = arq1.readlines()
        if senha + '\n' in registrados:
            self.mensagem["text"] = "Autenticado"
            arq.close()
            self.calc()

            if usuario + '\n' in registrados1:
                self.mensagem["text"] = "Autenticado"
                arq.close()
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

root = Tk()

Application(root)
root.mainloop()


