# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import logging
import os

# Configura��o do logging
logging.basicConfig(filename='captura_codigos.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Fun��o para salvar o codigo em um arquivo
def salvar_codigo(codigo):
    try:
        with open("codigos_capturados.txt", "a") as file:
            file.write(f"{codigo}\n")
        logging.info(f"codigo salvo: {codigo}")
    except Exception as e:
        logging.error(f"Erro ao salvar o codigo: {e}")
        messagebox.showerror("Erro", f"Nao foi possivel salvar o codigo: {e}")

# Fun��o chamada quando o bot�o � pressionado
def capturar_codigo():
    codigo = entrada_codigo.get()  # Obt�m o valor inserido no campo
    if codigo:
        messagebox.showinfo("codigo de Barras", f"codigo Capturado: {codigo}")
        salvar_codigo(codigo)  # Salva o codigo no arquivo de texto
        entrada_codigo.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        messagebox.showwarning("Aviso", "Por favor, insira um codigo de barras!")

# Fun��o para fechar a aplica��o
def fechar_janela():
    logging.info("Aplicacao encerrada pelo usuario.")
    janela.quit()

# Cria��o da janela principal
janela = tk.Tk()
janela.title("Gestao Vintage - Coletor Estacio")

# Define o tamanho da janela
janela.geometry("300x150")

# Label (r�tulo) para o campo de entrada
label_codigo = tk.Label(janela, text="Escaneie o codigo de Barras:")
label_codigo.pack(pady=10)

# Campo de entrada de texto
entrada_codigo = tk.Entry(janela, width=30)
entrada_codigo.pack(pady=5)

# Bot�o para capturar o codigo de barras
botao_capturar = tk.Button(janela, text="Capturar codigo", command=capturar_codigo)
botao_capturar.pack(pady=5)

# Bot�o para fechar a janela
botao_fechar = tk.Button(janela, text="Fechar", command=fechar_janela)
botao_fechar.pack(pady=5)

# Registro do in�cio da aplica��o
logging.info("Aplicacao iniciada.")

# Inicia o loop principal da interface
janela.mainloop()
