import tkinter as tk
from tkinter import messagebox

def entrar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == 'lu' and senha == '123':
        messagebox.showinfo('Login', 'Bem vindo')
    else:
        messagebox.showerror('Erro', 'Login e senha incorreta')
        

janela = tk.Tk()
Janela = janela.title('Tela de login')

tk.Label(janela, text='Login').pack()
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

tk.Label(janela, text='Senha').pack()
entrada_senha = tk.Entry(janela, show='*')
entrada_senha.pack()

botao = tk.Button(janela, text='entrar', command=entrar)
botao.pack()

janela.mainloop()


