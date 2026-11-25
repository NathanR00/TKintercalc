import tkinter as tk

#Variável de sinal e conta
sinal = "+"
conta = "0"

#Função dos números
def digitar(numero):
    if visor.get() == "Digite um número" or visor.get() == "Erro: Não existe divisão por 0" or visor.get() == "Erro":
        visor.delete(0, tk.END)
    visor.insert(tk.END, numero)

#Funções de limpeza
def limpar():
    visor.delete(0, tk.END)
    global conta
    global sinal
    conta = "0"
    sinal = "+"

def apagar():
    visor.delete(len(visor.get())-1, tk.END)


#Funções de operação
def somar():
    if visor.get() == "Digite um número" or visor.get() == "Erro: Não existe divisão por 0" or visor.get() == "Erro":
        visor.delete(0, tk.END)
        pass
    
    global conta
    global sinal
    
    try:
        numNovo = visor.get()
        conta = str(eval(f"{conta}{sinal}{numNovo}"))
        sinal = "+"
    
        visor.delete(0, tk.END)
    
    except Exception:
        visor_txt.set("Digite um número")

def subtrair():
    if visor.get() == "Digite um número" or visor.get() == "Erro: Não existe divisão por 0" or visor.get() == "Erro":
        visor.delete(0, tk.END)
        pass
    
    global conta
    global sinal
    
    try:
        numNovo = visor.get()
        conta = str(eval(f"{conta}{sinal}{numNovo}"))
        sinal = "-"
    
        visor.delete(0, tk.END)
    
    except Exception:
        visor_txt.set("Digite um número")

def multiplicar():
    if visor.get() == "Digite um número" or visor.get() == "Erro: Não existe divisão por 0" or visor.get() == "Erro":
        visor.delete(0, tk.END)
        pass
        
    global conta
    global sinal
    
    try:
        numNovo = visor.get()
        conta = str(eval(f"{conta}{sinal}{numNovo}"))
        sinal = "*"
    
        visor.delete(0, tk.END)
    
    except Exception:
        visor_txt.set("Digite um número")
    
def dividir():
    if visor.get() == "Digite um número" or visor.get() == "Erro: Não existe divisão por 0" or visor.get() == "Erro":
        visor.delete(0, tk.END)
        pass
        
    global conta
    global sinal
    
    try:
        numNovo = visor.get()
        conta = str(eval(f"{conta}{sinal}{numNovo}"))
        sinal = "/"
    
        visor.delete(0, tk.END)
    
    except Exception:
        visor_txt.set("Digite um número")
    
def igual():
    try:
        if visor.get().strip() == "":
            visor_txt.set("Digite um número")
        else:
            
            global conta
            global sinal
            
            numNovo = visor.get()
            conta = str(eval(f"{conta}{sinal}{numNovo}"))
            
            visor_txt.set(conta)
            
            conta = "0"
            sinal = "+"

    except ZeroDivisionError:
        visor_txt.set("Erro: Não existe divisão por 0")
        conta = "0"
        sinal = "+"
        
    except Exception:
        visor_txt.set("Erro")
        conta = "0"
        sinal = "+"
        
        

#Criação da tela
janela = tk.Tk()
janela.title("Calculadora Simples")

visor_txt = tk.StringVar();

#Visor da calculadora
visor = tk.Entry(janela, textvariable=visor_txt, width=32, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botão de limpar
botao_c = tk.Button(
    janela,
    text="C",
    width=6,
    height=2,
    command=limpar
)
botao_c.grid(row=1, column=0, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botão de apagar
botao_apagar = tk.Button(
    janela,
    text="⌫",
    width=6,
    height=2,
    command=apagar
)
botao_apagar.grid(row=1, column=1, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botão de divisão
botao_dividir = tk.Button(
    janela,
    text="÷",
    width=6,
    height=2,
    command=dividir
)
botao_dividir.grid(row=1, column=2, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botão de multiplicar
botao_multiplicar = tk.Button(
    janela,
    text="x",
    width=6,
    height=2,
    command=multiplicar
)
botao_multiplicar.grid(row=1, column=3, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botão de subtrair
botao_subtrair = tk.Button(
    janela,
    text="-",
    width=6,
    height=2,
    command=subtrair
)
botao_subtrair.grid(row=2, column=3, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botão de somar
botao_somar = tk.Button(
    janela,
    text="+",
    width=6,
    height=2,
    command=somar
)
botao_somar.grid(row=3, column=3, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)


# Botão de ponto
botao_ponto = tk.Button(
    janela,
    text=".",
    width=6,
    height=2,
    command=lambda: digitar(".")
)
botao_ponto.grid(row=5, column=2, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botões numéricos
botao_7 = tk.Button(
    janela,
    text="7",
    height=2,
    width=6,
    command=lambda: digitar("7")
)
botao_7.grid(row=2, column=0, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_8 = tk.Button(
    janela,
    text="8",
    height=2,
    width=6,
    command=lambda: digitar("8")
)
botao_8.grid(row=2, column=1, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_9 = tk.Button(
    janela,
    text="9",
    height=2,
    width=6,
    command=lambda: digitar("9")
)
botao_9.grid(row=2, column=2, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_4 = tk.Button(
    janela,
    text="4",
    width=6,
    height=2,
    command=lambda: digitar("4")
)
botao_4.grid(row=3, column=0, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_5 = tk.Button(
    janela,
    text="5",
    width=6,
    height=2,
    command=lambda: digitar("5")
)
botao_5.grid(row=3, column=1, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_6 = tk.Button(
    janela,
    text="6",
    width=6,
    height=2,
    command=lambda: digitar("6")
)
botao_6.grid(row=3, column=2, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_1 = tk.Button(
    janela,
    text="1",
    width=6,
    height=2,
    command=lambda: digitar("1")
)
botao_1.grid(row=4, column=0, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_2 = tk.Button(
    janela,
    text="2",
    width=6,
    height=2,
    command=lambda: digitar("2")
)
botao_2.grid(row=4, column=1, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

botao_3 = tk.Button(
    janela,
    text="3",
    width=6,
    height=2,
    command=lambda: digitar("3")
)
botao_3.grid(row=4, column=2, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=1)

# Botão de igual (l4 c3 | 2 linhas na vertical)
botao_igual = tk.Button(
    janela,
    text="=",
    width=6,
    height=5,
    command=igual
)
botao_igual.grid(row=4, column=3, padx=2, pady=2, sticky="nsew", columnspan=1, rowspan=2)

# Botão 0 (l5 c0 | 2 colunas na horizontal)
botao_0 = tk.Button(
    janela,
    text="0",
    width=15,
    height=2,
    command=lambda: digitar("0")
)
botao_0.grid(row=5, column=0, padx=2, pady=2, sticky="nsew", columnspan=2, rowspan=1)


# Configura o peso das linhas e colunas para distribuírem o espaço de forma igualitária
for i in range(1, 6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
    
janela.mainloop()