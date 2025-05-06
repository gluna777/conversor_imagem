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

# Criação da janela
janela = Tk()
janela.title("Tranforme sua foto em desenho a lápis")
janela.geometry('900x600')
janela.configure(bg=co8)
janela.resizable(width=FALSE, height=FALSE)


janela.mainloop()

