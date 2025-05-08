#Importação de bibliotecas

from tkinter import *
from tkinter import Tk, ttk, filedialog
from PIL import ImageTk, Image, ImageEnhance
import cv2
import os

# Cores utlizadas

co0 = "#f0f3f5"  # Preto
co1 = "#feffff"  # Branco
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # Profit
co6 = "#038cfc"  # Azul
co7 = "#1c1c1c"  # Preto moderno (mais realista)
co8 = "#f7f9f9"  # Branco gelo (mais suave que o branco puro)
co9 = "#2ecc71"  # Verde esmeralda (limpo e atual)
co10 = "#2c3e50"  # Azul petróleo escuro (substituto elegante para valores)
co11 = "#7f8c8d"  # Cinza médio (ótimo para textos)
co12 = "#f39c12"  # Laranja queimado (ótimo para destaque como lucros)
co13 = "#3498db"  # Azul padrão moderno (vivo, mas elegante)
co14 = "#ecf0f1"  # Cinza muito claro (quase branco, ótimo como fundo suave)
co15 = "#dfe6e9"  # Cinza gelo (clean e moderno, neutro)
co16 = "#bdc3c7"  # Cinza claro (bom para bordas ou divisores discretos)
co17 = "#95a5a6"  # Cinza neutro (para textos secundários ou ícones)
co18 = "#ffffff"  # Branco puro (ideal para contraste total)
co19 = "#f5f5f5"  # Branco fosco (menos brilho que o puro, mais confortável)
co20 = "#e0e0e0"  # Cinza leve (bom para áreas de fundo ou contornos suaves)

# Criação da janela
janela = Tk()
janela.title("Tranforme sua foto em desenho a lápis")
janela.geometry('1000x680')
janela.configure(bg=co8)
janela.resizable(width=FALSE, height=FALSE)


frame_top = Frame(janela, width=950, height=90, background=co1)
frame_top.grid(row=0, column=0, padx=10, pady=5)

frame_preview = Frame(janela, width=980, height=350, background=co16)
frame_preview.grid(row=1, column=0, padx=10, pady=5)

frame_controls = Frame(janela, width=980, height=200, background=co20)
frame_controls.grid(row=2, column=0, padx=10, pady=5)

# Logo e título
logo = Label(frame_top, text="Tranforme Qualquer Imagem em um Desenho a Lápis", 
             font=("Arial", 16, "bold"), background=co1, foreground=co11)
logo.pack()

# Previews
preview_original = Label(frame_preview, text="Imagem original", 
             font=("Arial", 12), background=co16, foreground=co11)
preview_original.place(x=0, y=15)

preview_convertida = Label(frame_preview, text="Imagem convertida", 
             font=("Arial", 12), background=co16, foreground=co11)
preview_convertida.place(x=490, y=15)

# Controls
ttk.Label(frame_controls, text="Intensidade", font=("Comic Sans MS", 10), background=co13, foreground=co7).place(x=10, y=5)
scale_intensidade = Scale(frame_controls, from_=0, to=100, orient=HORIZONTAL, 
                          length=950, background=co1, foreground=co12)
scale_intensidade.set(50)
scale_intensidade.place(x=10, y=25)

ttk.Label(frame_controls, text="Brilho", font=("Comic Sans MS", 10),background=co13, foreground=co7).place(x=10, y=70)
scale_brilho = Scale(frame_controls, from_=0, to=100, orient=HORIZONTAL, 
                          length=950, background=co1, foreground=co12)
scale_brilho.set(50)
scale_brilho.place(x=10, y=90)

ttk.Label(frame_controls, text="Contraste", font=("Comic Sans MS", 10), background=co13, foreground=co7).place(x=10, y=135)
scale_contraste = Scale(frame_controls, from_=0, to=100, orient=HORIZONTAL, 
                          length=950, background=co1, foreground=co12)
scale_contraste.set(50)
scale_contraste.place(x=10, y=155)

# Buttons
button_escolher = Button(janela, text="Escolher Imagem", background=co13, foreground=co1, 
                         font=("Arial", 10), width=35)
button_escolher.place(x=10, y=630)

button_converter = Button(janela, text="Converter", background=co9, foreground=co1, 
                         font=("Arial", 10), width=35)
button_converter.place(x=355, y=630)

button_salvar = Button(janela, text="Salvar Imagem", background=co12, foreground=co1, 
                         font=("Arial", 10), width=35)
button_salvar.place(x=700, y=630)


janela.mainloop()

