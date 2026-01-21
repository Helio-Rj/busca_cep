"""
Busca_Cep.py
Aplicativo para consulta de endereço por CEP via interface gráfica Tkinter e API brazilcep
Autor: Hélio do Nascimento Silva.
Versão: 1.0.0.1
Data: 20/01/2026

Descrição:
Este software permite ao usuário consultar dados de endereço a partir de um CEP brasileiro, exibindo as informações em uma interface intuitiva. Utiliza a biblioteca brazilcep para integração com serviços de consulta de CEP.

Requisitos:
- Python 3.7 ou superior
- Bibliotecas: tkinter, requests, brazilcep

Modo de uso:
1. Digite o CEP desejado no campo indicado.
2. Clique em "Buscar" para consultar o endereço.
3. Os campos de endereço, bairro, cidade e UF serão preenchidos automaticamente.
4. Para limpar os campos, clique em "Limpar".
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
import requests
import brazilcep

# Instancia a janela principal da aplicação
root = Tk()

class Validadores:
    """
    Fornece métodos de validação para entradas do usuário.
    """
    def validate_entry(self, text):
        """
        Valida se o texto inserido é um número inteiro dentro do intervalo permitido para CEP.
        Retorna True se válido, False caso contrário.
        """
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000

class Funcs:
    """
    Contém funções utilitárias para manipulação dos campos da interface.
    """
    def limpar_tela(self):
        """
        Limpa todos os campos de entrada da interface gráfica.
        """
        self.busca_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.uf_entry.delete(0, END)

class Aplication(Funcs, Validadores):
    """
    Gerencia toda a lógica da aplicação, inicialização da interface, eventos e integração com a API de consulta de CEP.
    """
    def __init__(self):
        """
        Inicializa a interface, configura widgets, menus e inicia o loop principal da aplicação.
        """
        self.root = root
        self.valida_entradas()
        self.tela()
        self.frames_tela()
        self.widiget_frame_1()
        self.Menus()
        root.mainloop()

    def cep_correios(self):
        """
        Realiza a consulta do endereço a partir do CEP informado pelo usuário.
        Preenche os campos de endereço, bairro, cidade e UF com os dados retornados.
        Em caso de erro, exibe mensagem informativa ao usuário.
        """
        try:
            self.endereco_entry.delete(0, END)
            self.bairro_entry.delete(0, END)
            self.cidade_entry.delete(0, END)
            self.uf_entry.delete(0, END)
            zipcose = self.busca_entry.get()
            dadoscep = brazilcep.get_address_from_cep(zipcose)
            self.endereco_entry.insert(END, dadoscep['street'])
            self.bairro_entry.insert(END, dadoscep['district'])
            self.cidade_entry.insert(END, dadoscep['city'])
            self.uf_entry.insert(END, dadoscep['uf'])
        except Exception:
            messagebox.showinfo('OPS...', 'CEP incorreto ou incompleto')

    def tela(self):
        """
        Configura propriedades visuais da janela principal, como título, cor de fundo,
        tamanho inicial, limites de redimensionamento e ícone.
        """
        # Ícone personalizado pode ser configurado aqui
        self.root.title("Busca CEP      Version 1.0.0.1")
        self.root.config(bg="#7070ff")
        self.root.geometry("400x200")
        self.root.resizable(True, True)
        self.root.maxsize(width=950, height=650)
        self.root.minsize(width=550, height=350)

    def frames_tela(self):
        """
        Cria e posiciona o frame principal da interface, onde os widgets serão inseridos.
        """
        self.frame_1 = Frame(self.root, bd=4, bg='#ffff00', highlightbackground='#1a0080', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widiget_frame_1(self):
        """
        Adiciona e posiciona todos os widgets (botões, labels, campos de entrada) no frame principal.
        """
        # Botão para buscar o CEP informado
        self.btn_buscar = Button(self.frame_1, text='Buscar', bd=2, bg="#4169E1", fg="#ffffff",
                                 font=('verdana', 8, 'bold'), command=self.cep_correios)
        self.btn_buscar.place(relx=0.60, rely=0.30, relwidth=0.12, relheight=0.07)

        # Botão para limpar todos os campos da interface
        self.btn_limpar = Button(self.frame_1, text='Limpar', bd=2, bg="#4169E1", fg="#ffffff",
                                 font=('verdana', 8, 'bold'), command=self.limpar_tela)
        self.btn_limpar.place(relx=0.45, rely=0.30, relwidth=0.12, relheight=0.07)

        # Título principal da interface
        self.lb_titulo = Label(self.frame_1, text="Faça sua busca pelo CEP:", bg="#ffff00", fg="#4169E1", font=('verdana', 15, 'bold'))
        self.lb_titulo.place(relx=0.05, rely=0.05)

        # Label para campo de busca do CEP
        self.lb_busca = Label(self.frame_1, text="Digite um CEP para busca:", bg="#ffff00", fg="#4169E1", font=('verdana', 9, 'bold'))
        self.lb_busca.place(relx=0.05, rely=0.20)

        # Label para campo de endereço
        self.lb_endereco = Label(self.frame_1, text="Endereço", bg="#ffff00", fg="#4169E1", font=('verdana', 9, 'bold'))
        self.lb_endereco.place(relx=0.05, rely=0.45)

        # Label para campo de cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade:", bg="#ffff00", fg="#4169E1", font=('verdana', 9, 'bold'))
        self.lb_cidade.place(relx=0.05, rely=0.65)

        # Label para campo de bairro
        self.lb_bairro = Label(self.frame_1, text="Bairro:", bg="#ffff00", fg="#4169E1", font=('verdana', 9, 'bold'))
        self.lb_bairro.place(relx=0.65, rely=0.45)

        # Label para campo de UF
        self.lb_UF = Label(self.frame_1, text="UF:", bg="#ffff00", fg="#4169E1", font=('verdana', 9, 'bold'))
        self.lb_UF.place(relx=0.65, rely=0.65)

        # Campo de entrada para o CEP
        self.busca_entry = Entry(self.frame_1, validate="key", validatecommand=self.vcmd2, bg="#FFFFF0", fg="#000000", font=('verdana', 12, 'bold'))
        self.busca_entry.place(relx=0.05, rely=0.30, relwidth=0.37, relheight=0.08)

        # Campo de entrada para o endereço
        self.endereco_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000", font=('verdana', 12, 'bold'))
        self.endereco_entry.place(relx=0.05, rely=0.55, relwidth=0.50, relheight=0.08)

        # Campo de entrada para o bairro
        self.bairro_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000", font=('verdana', 12, 'bold'))
        self.bairro_entry.place(relx=0.65, rely=0.55, relwidth=0.30, relheight=0.08)

        # Campo de entrada para a cidade
        self.cidade_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000", font=('verdana', 12, 'bold'))
        self.cidade_entry.place(relx=0.05, rely=0.75, relwidth=0.50, relheight=0.08)

        # Campo de entrada para a UF
        self.uf_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000", font=('verdana', 12, 'bold'))
        self.uf_entry.place(relx=0.65, rely=0.75, relwidth=0.07, relheight=0.08)

    def Menus(self):
        """
        Cria e configura a barra de menus da aplicação, incluindo opções de sair e informações sobre o desenvolvedor.
        """
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit():
            """Encerra a aplicação."""
            self.root.destroy()
        menubar.add_cascade(label="Sobre", menu=filemenu2)
        menubar.add_cascade(label="Sair", menu=filemenu)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu2.add_command(label="Desenvolvido Pela Puritoka Zaybatsu Inc.")

    def valida_entradas(self):
        """
        Configura o método de validação para o campo de entrada do CEP, permitindo apenas valores válidos.
        """
        self.vcmd2 = (self.root.register(self.validate_entry), "%P")

# Inicializa a aplicação
Aplication()
