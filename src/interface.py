import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import main

janela = tk.Tk()
janela.title("Dashboard Interativo de Análise de Risco")
janela.geometry("650x600")
janela.configure(bg="#f4f4f4")

df = None

caminho_padrao = "assets/dados.csv"

def carregar_dados():
    global df
    try:
        df = main.ler_csv(caminho_padrao)
        messagebox.showinfo("Sucesso", "Dados carregados e coluna 'risco' calculada!")
    except FileNotFoundError:
        messagebox.showerror("Erro", f"O arquivo '{caminho_padrao}' não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao carregar dados: {e}")

def grafico_pizza_idade():
    global df
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    main.gerar_grafico_pizza_idade(df)

def grafico_pizza_risco():
    global df
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    main.gerar_grafico_pizza_risco(df)

def grafico_pizza_renda():
    global df
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    main.gerar_grafico_pizza_renda(df)

def grafico_barras_imc_por_renda():
    global df
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    main.gerar_grafico_barras_empilhadas(df)

def gerar_fila_ordenada():
    global df
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    try:
        main.salvar_lista_ordenada(df)
        messagebox.showinfo("Info", "Fila ordenada salva com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível salvar a fila: {e}")

titulo = tk.Label(
    janela,
    text="Painel Interativo de Análise de Riscos",
    font=("Helvetica", 18, "bold"),
    bg="#f4f4f4",
    fg="#333",
)
titulo.pack(pady=20)

btn_carregar = tk.Button(
    janela,
    text="📂 Carregar Dados (Calcula 'risco')",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=30,
    command=carregar_dados,
)
btn_carregar.pack(pady=10)

frame_graficos = tk.Frame(janela, bg="#f4f4f4")
frame_graficos.pack(pady=20)

label_graficos = tk.Label(
    frame_graficos,
    text="Escolha um gráfico para visualizar:",
    font=("Helvetica", 14),
    bg="#f4f4f4",
    fg="#222",
)
label_graficos.grid(row=0, column=0, columnspan=2, pady=(0, 15))

botoes_graficos = [
    ("🎂 Pizza: Faixas Etárias", grafico_pizza_idade, 1, 0),
    ("📊 Pizza: Faixas de Risco", grafico_pizza_risco, 1, 1),
    ("💰 Pizza: Faixas de Renda", grafico_pizza_renda, 2, 0),
    ("📶 Barras: IMC por Renda", grafico_barras_imc_por_renda, 2, 1),
]

for texto, func, linha, coluna in botoes_graficos:
    btn = tk.Button(
        frame_graficos,
        text=texto,
        font=("Helvetica", 11),
        bg="#2196F3",
        fg="white",
        width=30,
        command=func,
    )
    btn.grid(row=linha, column=coluna, padx=10, pady=7)

btn_fila = tk.Button(
    janela,
    text="🗂️ Gerar Fila Ordenada (Salvar CSV)",
    font=("Helvetica", 12, "bold"),
    bg="#FF5722",
    fg="white",
    width=35,
    command=gerar_fila_ordenada,
)
btn_fila.pack(pady=25)

rodape = tk.Label(
    janela,
    text="© 2025 Projeto - Fila de Espera para Cirurgia Bariátrica.",
    font=("Helvetica", 9),
    bg="#f4f4f4",
    fg="#666",
)
rodape.pack(side="bottom", pady=15)

janela.mainloop()