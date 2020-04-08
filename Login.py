import sys
import pymysql.cursors
from conexaoBD import BD
from index import Index

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class JanelaLogin:
    def __init__(self):
        '''Variaveis'''
        self.logado = False

        self.top = tk.Tk()

        font10 = "-family SimSun-ExtB -size 15 -weight normal -slant "  \
        "roman -underline 0 -overstrike 0"
        font9 = "-family SimSun-ExtB -size 22 -weight normal -slant "  \
        "roman -underline 0 -overstrike 0"


        self.top.geometry("715x742+535+150")
        self.top.title("New Toplevel")
        self.top.configure(background="#181B24")

        Frame1 = tk.Frame(self.top)
        Frame1.place(relx=0.21, rely=0.216, relheight=0.559, relwidth=0.594)

        Frame1.configure(relief='flat')
        Frame1.configure(borderwidth="2")
        Frame1.configure(background="#878B96")

        Label1 = tk.Label(Frame1)
        Label1.place(relx=0.341, rely=0.048, height=41, width=134)
        Label1.configure(background="#878B96")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font9)
        Label1.configure(foreground="#ffffff")
        Label1.configure(text='''SOFIA''')


        Label2 = tk.Label(Frame1)
        Label2.place(relx=0.188, rely=0.193, height=21, width=74)
        Label2.configure(activebackground="#f0f0f0")
        Label2.configure(background="#878B96")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=font10)
        Label2.configure(foreground="#ffffff")
        Label2.configure(text='''Usuario''')


        self.Entry1 = tk.Entry(Frame1)
        self.Entry1.place(relx=0.188, rely=0.265,height=20, relwidth=0.621)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")


        Label2_1 = tk.Label(Frame1)
        Label2_1.place(relx=0.165, rely=0.361, height=21, width=74)
        Label2_1.configure(activebackground="#f0f0f0")
        Label2_1.configure(activeforeground="black")
        Label2_1.configure(background="#878B96")
        Label2_1.configure(disabledforeground="#a3a3a3")
        Label2_1.configure(font=font10)
        Label2_1.configure(foreground="#ffffff")
        Label2_1.configure(highlightbackground="#d9d9d9")
        Label2_1.configure(highlightcolor="black")
        Label2_1.configure(text='''Senha''')

        self.Entry1_2 = tk.Entry(Frame1, show='*')
        self.Entry1_2.place(relx=0.188, rely=0.434,height=20, relwidth=0.621)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        Button1 = tk.Button(Frame1, command=self.verificaLogin)
        Button1.place(relx=0.212, rely=0.53, height=44, width=117)
        Button1.configure(activebackground="#a8a8a8")
        Button1.configure(activeforeground="#000000")
        Button1.configure(background="#878B96")
        Button1.configure(disabledforeground="#a3a3a3")
        Button1.configure(font=font10)
        Button1.configure(foreground="#ffffff")
        Button1.configure(highlightbackground="#d9d9d9")
        Button1.configure(highlightcolor="black")
        Button1.configure(pady="0")
        Button1.configure(relief="groove")
        Button1.configure(text='''Logar''')

        Button1_3 = tk.Button(Frame1)
        Button1_3.place(relx=0.518, rely=0.53, height=44, width=117)
        Button1_3.configure(activebackground="#a8a8a8")
        Button1_3.configure(activeforeground="#000000")
        Button1_3.configure(background="#4b327f")
        Button1_3.configure(disabledforeground="#a3a3a3")
        Button1_3.configure(font=font10)
        Button1_3.configure(foreground="#ffffff")
        Button1_3.configure(highlightbackground="#d9d9d9")
        Button1_3.configure(highlightcolor="black")
        Button1_3.configure(pady="0")
        Button1_3.configure(relief="flat")
        Button1_3.configure(text='''Criar conta''')

        Button2 = tk.Button(Frame1)
        Button2.place(relx=-0.024, rely=0.916, height=33, width=205)
        Button2.configure(activebackground="#ececec")
        Button2.configure(activeforeground="#000000")
        Button2.configure(background="#878B96")
        Button2.configure(disabledforeground="#a3a3a3")
        Button2.configure(font=font10)
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(relief="flat")
        Button2.configure(text='''Entrar sem login''')

        Button2_4 = tk.Button(Frame1)
        Button2_4.place(relx=0.494, rely=0.916, height=33, width=225)
        Button2_4.configure(activebackground="#ececec")
        Button2_4.configure(activeforeground="#000000")
        Button2_4.configure(background="#878B96")
        Button2_4.configure(disabledforeground="#a3a3a3")
        Button2_4.configure(font=font10)
        Button2_4.configure(foreground="#000000")
        Button2_4.configure(highlightbackground="#d9d9d9")
        Button2_4.configure(highlightcolor="black")
        Button2_4.configure(pady="0")
        Button2_4.configure(relief="flat")
        Button2_4.configure(text='''Esqueci minha senha''')

        TSeparator2 = ttk.Separator(Frame1)
        TSeparator2.place(relx=0.471, rely=0.94, relheight=0.048)
        TSeparator2.configure(orient="vertical")

        self.top.mainloop()

    def verificaLogin(self):
        usuario = self.Entry1.get()
        senha = self.Entry1_2.get()

        conexao = BD.conectar()
        resultado = BD.select(conexao, 'usuarios')
        existencia = False

        for dict in resultado:
            if dict['usuarios'] == usuario and dict['senha'] == senha:
                self.logado = True
                self.top.destroy()
                Index()






JanelaLogin()