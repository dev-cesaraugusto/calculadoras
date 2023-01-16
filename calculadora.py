import math
from tkinter import *

root = Tk()
root.title("Calculadora")

# Cria uma entrada de texto para exibir o resultado
resultado = Entry(root)
resultado.grid(row=0, column=0, columnspan=4)

# Define a função para realizar a operação matemática
def calcular():
    try:
        resultado.delete(0, END)
        resultado.insert(END, eval(entrada.get()))
    except:
        resultado.delete(0, END)
        resultado.insert(END, "ERRO")

# Define a função para limpar a entrada de texto
def clear():
    entrada.delete(0, END)
    resultado.delete(0, END)

# Cria os botões numéricos e de operação
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
operadores = ["+", "-", "*", "/"]

entrada = Entry(root)
entrada.grid(row=1, column=0, columnspan=4)

i = 2
for numero in numeros:
    btn = Button(root, text=numero, width=5, height=2, command=lambda num=numero: entrada.insert(END, num))
    btn.grid(row=i, column=0)
    i += 1

i = 2
for operador in operadores:
    btn = Button(root, text=operador, width=5, height=2, command=lambda op=operador: entrada.insert(END, op))
    btn.grid(row=i, column=1)
    i += 1

btn_clear = Button(root, text="C", width=5, height=2, command=clear)
btn_clear.grid(row=6, column=0)

btn_equal = Button(root, text="=", width=5, height=2, command=calcular)
btn_equal.grid(row=6, column=1)

root.mainloop()
