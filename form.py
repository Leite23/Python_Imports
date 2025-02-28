import tkinter as tk

def criar_formulario():
    janela = tk.Tk()
    janela.title("Formulário")

    tk.Label(janela, text="Nome:").grid(row=0, column=0)
    nome = tk.Entry(janela)
    nome.grid(row=0, column=1)

    tk.Label(janela, text="E-mail:").grid(row=1, column=0)
    email = tk.Entry(janela)
    email.grid(row=1, column=1)

    tk.Label(janela, text="Telefone:").grid(row=2, column=0)
    telefone = tk.Entry(janela)
    telefone.grid(row=2, column=1)

    def enviar_formulario():
        nome_digitado = nome.get()
        email_digitado = email.get()
        telefone_digitado = telefone.get()

        janela.destroy()

        janela_boas_vindas = tk.Tk()
        janela_boas_vindas.title("Bem-vindo!")

        label_boas_vindas = tk.Label(janela_boas_vindas, text=f"Bem-vindo, {nome_digitado}!")
        label_boas_vindas.pack()

        janela_boas_vindas.mainloop()

    tk.Button(janela, text="Enviar", command=enviar_formulario).grid(row=3, column=1)

    janela.mainloop()

criar_formulario()