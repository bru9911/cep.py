from tkinter import *

# Função para submeter o formulário
def submit():
    nome = nome_entry.get()
    email = email_entry.get()
    idade = idade_entry.get()
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Idade: {idade}")

# Cria a janela principal
janela = Tk()

# Define o título da janela
janela.title("Formulário")

# Cria os widgets do formulário
nome_label = Label(janela, text="Nome:")
nome_entry = Entry(janela)

email_label = Label(janela, text="E-mail:")
email_entry = Entry(janela)

idade_label = Label(janela, text="Idade:")
idade_entry = Entry(janela)

submit_button = Button(janela, text="Enviar", command=submit)

# Posiciona os widgets na janela
nome_label.grid(row=0, column=0)
nome_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

idade_label.grid(row=2, column=0)
idade_entry.grid(row=2, column=1)

submit_button.grid(row=3, column=1)

# Inicia a execução da janela
janela.mainloop()
