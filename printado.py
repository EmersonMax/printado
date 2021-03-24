import pyautogui
import getpass
import os
import tkinter as tk
from datetime import datetime

data_e_hora_atuais = datetime.now()

data = data_e_hora_atuais.strftime('%d_%m_%Y_%H_%M_%S')
user = getpass.getuser()
tela = tk.Tk()
tela.title('Printado')
tela.iconbitmap('ico.ico')

tela_principal = tk.Canvas(tela, width=140, height=100)
tela_principal.pack()



def printar():
    printado = pyautogui.screenshot()
    local = "C:\\users\\" + user + "\\printado"
    if os.path.isdir(local):
        printado.save(local + "\\printado" + data + ".png")
        tk.Label(tela, text="Print realizado com sucesso", bg="black", fg="white").pack()
    else:
        os.mkdir(local)
        printado.save(local + "\\printado" + data + ".png")
        tk.Label(tela, text="Print realizado com sucesso", bg="black", fg="white").pack()


botaoprint = tk.Button(text='Printar a Tela', command=printar, bg='black', fg='white', font=10)
botaoprint.pack( padx="60", pady="60", fill= "both", expand="1" )
tela_principal.create_window(70, 30, window=botaoprint)

tk.Label(tela, text="Emerson Max", fg="black", font=1).pack()

tela.mainloop()

