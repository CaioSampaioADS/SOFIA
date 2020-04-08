import tkinter as tk
import tkinter.ttk as ttk
import sys


class BaseIndex:
    def __init__(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family SimSun-ExtB -size 14 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font14 = "-family SimSun-ExtB -size 13 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"

        top = tk.Tk()

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1459x890+162+76")
        top.title("New Toplevel")
        top.configure(background="#878b96")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Arquivos")
        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Algoritmos")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.017, relwidth=0.161)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#26242F")

        self.BtnKNN = tk.Button(self.Frame1)
        self.BtnKNN.place(relx=0.0, rely=0.011, height=64, width=237)
        self.BtnKNN.configure(activebackground="#181B24")
        self.BtnKNN.configure(activeforeground="white")
        self.BtnKNN.configure(activeforeground="#000000")
        self.BtnKNN.configure(background="#181B24")
        self.BtnKNN.configure(disabledforeground="#a3a3a3")
        self.BtnKNN.configure(font=font10)
        self.BtnKNN.configure(foreground="#ffffff")
        self.BtnKNN.configure(highlightbackground="#d9d9d9")
        self.BtnKNN.configure(highlightcolor="black")
        self.BtnKNN.configure(pady="0")
        self.BtnKNN.configure(relief="flat")
        self.BtnKNN.configure(text='''KNN''')

        self.BtnRegLog = tk.Button(self.Frame1)
        self.BtnRegLog.place(relx=0.0, rely=0.11, height=64, width=237)
        self.BtnRegLog.configure(activebackground="#181B24")
        self.BtnRegLog.configure(activeforeground="white")
        self.BtnRegLog.configure(activeforeground="#000000")
        self.BtnRegLog.configure(background="#181B24")
        self.BtnRegLog.configure(disabledforeground="#a3a3a3")
        self.BtnRegLog.configure(font=font10)
        self.BtnRegLog.configure(foreground="#ffffff")
        self.BtnRegLog.configure(highlightbackground="#d9d9d9")
        self.BtnRegLog.configure(highlightcolor="black")
        self.BtnRegLog.configure(pady="0")
        self.BtnRegLog.configure(relief="flat")
        self.BtnRegLog.configure(text='''Regressão Logística''')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.064, rely=0.21, relwidth=0.851)

        self.BtnRegLine = tk.Button(self.Frame1)
        self.BtnRegLine.place(relx=0.0, rely=0.243, height=64, width=237)
        self.BtnRegLine.configure(activebackground="#181B24")
        self.BtnRegLine.configure(activeforeground="white")
        self.BtnRegLine.configure(activeforeground="#000000")
        self.BtnRegLine.configure(background="#181B24")
        self.BtnRegLine.configure(disabledforeground="#a3a3a3")
        self.BtnRegLine.configure(font=font10)
        self.BtnRegLine.configure(foreground="#ffffff")
        self.BtnRegLine.configure(highlightbackground="#d9d9d9")
        self.BtnRegLine.configure(highlightcolor="black")
        self.BtnRegLine.configure(pady="0")
        self.BtnRegLine.configure(relief="flat")
        self.BtnRegLine.configure(text='''Regressão Linear''')

        self.BtnRegLineMult = tk.Button(self.Frame1)
        self.BtnRegLineMult.place(relx=0.0, rely=0.343, height=74, width=237)
        self.BtnRegLineMult.configure(activebackground="#181B24")
        self.BtnRegLineMult.configure(activeforeground="white")
        self.BtnRegLineMult.configure(activeforeground="#000000")
        self.BtnRegLineMult.configure(background="#181B24")
        self.BtnRegLineMult.configure(disabledforeground="#a3a3a3")
        self.BtnRegLineMult.configure(font=font14)
        self.BtnRegLineMult.configure(foreground="#ffffff")
        self.BtnRegLineMult.configure(highlightbackground="#d9d9d9")
        self.BtnRegLineMult.configure(highlightcolor="black")
        self.BtnRegLineMult.configure(pady="0")
        self.BtnRegLineMult.configure(relief="flat")
        self.BtnRegLineMult.configure(text='''Regressão Linear Multipla''')

        self.BtnPerfil = tk.Button(top)
        self.BtnPerfil.place(relx=0.946, rely=0.011, height=64, width=67)
        self.BtnPerfil.configure(activebackground="#ececec")
        self.BtnPerfil.configure(activeforeground="#000000")
        self.BtnPerfil.configure(background="#d9d9d9")
        self.BtnPerfil.configure(disabledforeground="#a3a3a3")
        self.BtnPerfil.configure(foreground="#000000")
        self.BtnPerfil.configure(highlightbackground="#d9d9d9")
        self.BtnPerfil.configure(highlightcolor="black")
        self.BtnPerfil.configure(pady="0")
        self.BtnPerfil.configure(relief="flat")
        self.BtnPerfil.configure(text='''Nome''')

        self.FrameGrafico = tk.Frame(top)
        self.FrameGrafico.place(relx=0.24, rely=0.079, relheight=0.421
                                , relwidth=0.332)
        self.FrameGrafico.configure(relief='groove')
        self.FrameGrafico.configure(borderwidth="2")
        self.FrameGrafico.configure(relief="groove")
        self.FrameGrafico.configure(background="#d9d9d9")

        self.ButtonGraficoPrincipal = tk.Button(top)
        self.ButtonGraficoPrincipal.place(relx=0.583, rely=0.09, height=44
                                          , width=197)
        self.ButtonGraficoPrincipal.configure(activebackground="#ececec")
        self.ButtonGraficoPrincipal.configure(activeforeground="#000000")
        self.ButtonGraficoPrincipal.configure(background="#878b96")
        self.ButtonGraficoPrincipal.configure(disabledforeground="#a3a3a3")
        self.ButtonGraficoPrincipal.configure(font=font10)
        self.ButtonGraficoPrincipal.configure(foreground="#000000")
        self.ButtonGraficoPrincipal.configure(highlightbackground="#d9d9d9")
        self.ButtonGraficoPrincipal.configure(highlightcolor="black")
        self.ButtonGraficoPrincipal.configure(pady="0")
        self.ButtonGraficoPrincipal.configure(relief="groove")
        self.ButtonGraficoPrincipal.configure(text='''Gráfico principal''')

        self.ButtonGraficoPrincipal_3 = tk.Button(top)
        self.ButtonGraficoPrincipal_3.place(relx=0.583, rely=0.157, height=44
                                            , width=197)
        self.ButtonGraficoPrincipal_3.configure(activebackground="#ececec")
        self.ButtonGraficoPrincipal_3.configure(activeforeground="#000000")
        self.ButtonGraficoPrincipal_3.configure(background="#878b96")
        self.ButtonGraficoPrincipal_3.configure(disabledforeground="#a3a3a3")
        self.ButtonGraficoPrincipal_3.configure(font=font10)
        self.ButtonGraficoPrincipal_3.configure(foreground="#000000")
        self.ButtonGraficoPrincipal_3.configure(highlightbackground="#d9d9d9")
        self.ButtonGraficoPrincipal_3.configure(highlightcolor="black")
        self.ButtonGraficoPrincipal_3.configure(pady="0")
        self.ButtonGraficoPrincipal_3.configure(relief="groove")
        self.ButtonGraficoPrincipal_3.configure(text='''Gráfico do Erro''')

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.26, rely=0.562, relwidth=0.466)

        self.BtnAcerto = tk.Button(top)
        self.BtnAcerto.place(relx=0.24, rely=0.607, height=34, width=137)
        self.BtnAcerto.configure(activebackground="#ececec")
        self.BtnAcerto.configure(activeforeground="#000000")
        self.BtnAcerto.configure(background="#878b96")
        self.BtnAcerto.configure(disabledforeground="#a3a3a3")
        self.BtnAcerto.configure(font=font10)
        self.BtnAcerto.configure(foreground="#000000")
        self.BtnAcerto.configure(highlightbackground="#d9d9d9")
        self.BtnAcerto.configure(highlightcolor="black")
        self.BtnAcerto.configure(pady="0")
        self.BtnAcerto.configure(relief="groove")
        self.BtnAcerto.configure(text='''% de acerto''')

        self.LabelAcerto = tk.Label(top)
        self.LabelAcerto.place(relx=0.336, rely=0.607, height=31, width=104)
        self.LabelAcerto.configure(background="#878b96")
        self.LabelAcerto.configure(disabledforeground="#a3a3a3")
        self.LabelAcerto.configure(foreground="#000000")

        self.ButtonGraficoPrincipal_4 = tk.Button(top)
        self.ButtonGraficoPrincipal_4.place(relx=0.583, rely=0.281, height=44
                                            , width=197)
        self.ButtonGraficoPrincipal_4.configure(activebackground="#ececec")
        self.ButtonGraficoPrincipal_4.configure(activeforeground="#000000")
        self.ButtonGraficoPrincipal_4.configure(background="#878b96")
        self.ButtonGraficoPrincipal_4.configure(disabledforeground="#a3a3a3")
        self.ButtonGraficoPrincipal_4.configure(font=font10)
        self.ButtonGraficoPrincipal_4.configure(foreground="#000000")
        self.ButtonGraficoPrincipal_4.configure(highlightbackground="#d9d9d9")
        self.ButtonGraficoPrincipal_4.configure(highlightcolor="black")
        self.ButtonGraficoPrincipal_4.configure(pady="0")
        self.ButtonGraficoPrincipal_4.configure(relief="groove")
        self.ButtonGraficoPrincipal_4.configure(text='''Prever''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.583, rely=0.236, height=20, relwidth=0.133)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.631, rely=0.348, height=31, width=54)
        self.Label1.configure(background="#878b96")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Label''')
        top.mainloop()


