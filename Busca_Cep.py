import tkinter as tk
from  tkinter import messagebox

from tkinter import *
from tkinter import PhotoImage
import requests
import brazilcep



root = Tk()


class Validadores():
    def validate_entry(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000



class Funcs():
    def limpar_tela(self):
        self.busca_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.uf_entry.delete(0, END)


class Aplication(Funcs, Validadores):
    def __init__(self):
        self.root = root        # Equivalência
        self.valida_entradas()  # Valida entradas numericas
        self.tela()             #toda a função "tela()"
        self.frames_tela()      # Chamada da função "frames_tela()"
        self.widiget_frame_1()  # Função dos botões.
        self.Menus()            # Função que governa os MenusBar
        root.mainloop()         # loop

    def cep_correios(self):
        try:
            self.endereco_entry.delete(0, END)
            self.bairro_entry.delete(0, END)
            self.cidade_entry.delete(0, END)
            self.uf_entry.delete(0, END)
            zipcose = self.busca_entry.get()
            dadoscep = brazilcep.get_address_from_cep(zipcose)
            print(dadoscep)
            self.endereco_entry.insert(END, dadoscep['street'])
            self.bairro_entry.insert(END, dadoscep['district'])
            self.cidade_entry.insert(END, dadoscep['city'])
            self.uf_entry.insert(END, dadoscep['uf'])
        except:
            messagebox.showinfo('OPS...', 'CEP incorreto ou incompleto')



    def tela(self):
        #self.root.iconbitmap("flatcon.ico")  # Coloca o flaticon
        self.root.title("Busca CEP      Version 1.0.0.1")# definição do texto título
        self.root.config(bg="#7070ff")  # configuração de cores fundo
        self.root.geometry("400x200")  # Altura e largura da tela em Pixels
        self.root.resizable(True, True) # Impede a maximização da janela quando em "False"
        self.root.maxsize(width=950, height=650)# Máximo tamanho permitido.
        self.root.minsize(width=550,height=350) # Minimo tamanho permitido.

    def frames_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#ffff00',highlightbackground='#1a0080', highlightthickness=3) # fina borda
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96 , relheight=0.96) # método para enquadramento de janela (Relative) por cordenadas

    def widiget_frame_1(self):
        # Botão buscar
        self.btn_buscar = Button(self.frame_1, text='Buscar', bd=2, bg="#4169E1", fg="#ffffff",
                                 font=('verdana', 8, 'bold'), command=self.cep_correios)  # Esse botão fica dentro do frame 1
        self.btn_buscar.place(relx=0.60, rely=0.30, relwidth=0.12, relheight=0.07)  # Posicionamento do botão limpar

        # botão Limpar
        self.btn_limpar = Button(self.frame_1, text='Limpar', bd=2, bg="#4169E1", fg="#ffffff",
                                 font=('verdana', 8, 'bold'),
                                 command=self.limpar_tela)  # Esse botão fica dentro do frame 1
        self.btn_limpar.place(relx=0.45, rely=0.30, relwidth=0.12, relheight=0.07)  # Posicionamento do botão limpar

        # bloco de configuração do "título"
        self.lb_titulo = Label(self.frame_1, text="Faça sua busca pelo CEP:", bg="#ffff00", fg="#4169E1",font=('verdana', 15, 'bold'))
        self.lb_titulo.place(relx=0.05, rely=0.05)

        # bloco de configuração dos "Labels"
        self.lb_busca = Label(self.frame_1, text="Digite um CEP para busca:", bg="#ffff00", fg="#4169E1", font=('verdana', 9, 'bold'))
        self.lb_busca.place(relx=0.05, rely=0.20)

        ### Endereço
        self.lb_endereco = Label(self.frame_1, text="Endereço", bg="#ffff00", fg="#4169E1",
                              font=('verdana', 9, 'bold'))
        self.lb_endereco.place(relx=0.05, rely=0.45)

        ###Cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade:", bg="#ffff00", fg="#4169E1",
                              font=('verdana', 9, 'bold'))
        self.lb_cidade.place(relx=0.05, rely=0.65)

        ###Bairro
        self.lb_bairro = Label(self.frame_1, text="Bairro:", bg="#ffff00", fg="#4169E1",
                              font=('verdana', 9, 'bold'))
        self.lb_bairro.place(relx=0.65, rely=0.45)

        ###Unidade Federativa (UF)
        self.lb_UF = Label(self.frame_1, text="UF:", bg="#ffff00", fg="#4169E1",
                               font=('verdana', 9, 'bold'))
        self.lb_UF.place(relx=0.65, rely=0.65)






        # Código para entrada "Entry"
        self.busca_entry = Entry(self.frame_1, validate="key", validatecommand= self.vcmd2 ,bg="#FFFFF0", fg="#000000",
                                font=('verdana', 12, 'bold'))  # codigo equivalente ao o "input"
        self.busca_entry.place(relx=0.05, rely=0.30, relwidth=0.37, relheight=0.08)

        ###Entry endereço
        self.endereco_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000",
                                 font=('verdana', 12, 'bold'))  # codigo equivalente ao o "input"
        self.endereco_entry.place(relx=0.05, rely=0.55, relwidth=0.50, relheight=0.08)

        ###Entry bairro
        self.bairro_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000",
                                    font=('verdana', 12, 'bold'))  # codigo equivalente ao o "input"
        self.bairro_entry.place(relx=0.65, rely=0.55, relwidth=0.30, relheight=0.08)

        ###Entry cidade
        self.cidade_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000",
                                  font=('verdana', 12, 'bold'))  # codigo equivalente ao o "input"
        self.cidade_entry.place(relx=0.05, rely=0.75, relwidth=0.50, relheight=0.08)

        ###Entry UF
        self.uf_entry = Entry(self.frame_1, bg="#FFFFF0", fg="#000000",
                                  font=('verdana', 12, 'bold'))  # codigo equivalente ao o "input"
        self.uf_entry.place(relx=0.65, rely=0.75, relwidth=0.07, relheight=0.08)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)


        # Variável para quitar
        def Quit(): self.root.destroy()
        menubar.add_cascade(label="Sobre", menu=filemenu2)
        menubar.add_cascade(label="Sair", menu=filemenu)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu2.add_command(label="Desenvolvido Pela Puritoka Zaybatsu Inc.")


    def valida_entradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry), "%P")


Aplication()
