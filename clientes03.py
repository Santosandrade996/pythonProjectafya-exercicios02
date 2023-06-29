import tkinter as tk
from tkinter import ttk
import datetime as dt


listas_nome = ['BMW S1000 RR', 'Honda CBR 650R ', 'Kawasaki Ninja ZX6']
listas_tipos = ['BMW S100 RR- 4.369', 'Honda CBR 650R- 4.310', 'Kawasaki Ninja ZX6- 39.754']
listas_registrados = ['Rodrigo Comprou a Motocicleta da marca BMW S1000RR']
janela = tk.Tk()


# Criação da função
def inserir_ok():
    descricao = combobox_selecionar_nome.get()
    tipo = combobox_selecionar_tipo.get()
    quant= combobox_selecionar_tipo.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%Y  %H:%M')



# Titulo da janela:
janela.title('Consulta de Vendas de Motocicletas')

label_marcasmotocicleta = tk.Label(text=' Marcas da Motocicletas')
label_marcasmotocicleta.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
combobox_selecionar_nome = ttk.Combobox(values=listas_nome)
combobox_selecionar_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_quantidadesvendidas = tk.Label(text='Quantidades de Vendas')
label_quantidadesvendidas.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
combobox_selecionar_tipo = ttk.Combobox(values=listas_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_clientes = tk.Label(text='Clientes Registrados')
label_clientes.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
combobox_selecionar_tipo = ttk.Combobox(values=listas_registrados)
combobox_selecionar_tipo.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)
botao_criar_ok = tk.Button(text='OK', command=inserir_ok)
botao_criar_ok.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()