import tkinter as tk
from tkinter import messagebox
import random
import string


def gerar_senha():
    try:
        tamanho = int(entrada_tamanho.get())
        if tamanho < 4:
            raise ValueError('Numero deve ser maior que 4')

        

        caracteres = string.ascii_letters + string.punctuation + string.digits
    
                
        senha = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        
        senha += random.choices(caracteres, k=tamanho - 4)
        random.shuffle(senha)

        senha_gerada.set(''.join(senha))
        
        
        

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Criar a janela
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("400x200")

# Variável para mostrar a senha
senha_gerada = tk.StringVar()

# Widgets
tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entrada_tamanho = tk.Entry(janela)
entrada_tamanho.pack()

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

tk.Label(janela, text="Senha Gerada:").pack()
tk.Entry(janela, textvariable=senha_gerada, width=30).pack()

# Rodar a janela
janela.mainloop()