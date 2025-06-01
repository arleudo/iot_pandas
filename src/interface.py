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
        df = pd.read_csv(caminho_padrao, sep=";")
        df["risco"] = df.apply(main.calcular_risco, axis=1)
        messagebox.showinfo("Sucesso", "Dados carregados e coluna 'risco' calculada!")
    except FileNotFoundError:
        messagebox.showerror("Erro", f"O arquivo '{caminho_padrao}' não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao carregar dados: {e}")

def grafico_pizza_idade():
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    faixas = pd.cut(df["idade"], bins=[0, 18, 40, 60, 80], labels=["0-18", "19-40", "41-60", "61-80"])
    distribuicao = faixas.value_counts().sort_index()

    win = tk.Toplevel(janela)
    win.title("Pizza: Faixas Etárias")
    win.geometry("500x500")
    win.configure(bg="#ffffff")

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    distribuicao.plot.pie(
        ax=ax,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
        labels=distribuicao.index,
    )
    ax.set_title("Distribuição de Idades (Faixas Etárias)")
    ax.set_ylabel("")

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def grafico_pizza_risco():
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    faixas = pd.cut(df["risco"], bins=[0, 15, 20, 25, 30], labels=["0-15", "16-20", "21-25", "26-30"])
    distribuicao = faixas.value_counts().sort_index()

    win = tk.Toplevel(janela)
    win.title("Pizza: Faixas de Risco")
    win.geometry("500x500")
    win.configure(bg="#ffffff")

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    distribuicao.plot.pie(
        ax=ax,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
        labels=distribuicao.index,
    )
    ax.set_title("Distribuição de Risco")
    ax.set_ylabel("")

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def grafico_pizza_renda():
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    faixas = pd.cut(
        df["rendaFamiliar"],
        bins=[0, 1, 2, 3, 4, 5],
        labels=[
            "Até 1 salário mínimo",
            "Até 2 salários mínimos",
            "Até 3 salários mínimos",
            "Até 4 salários mínimos",
            "5 salários mínimos ou mais",
        ],
    )
    distribuicao = faixas.value_counts().sort_index()

    win = tk.Toplevel(janela)
    win.title("Pizza: Faixas de Renda")
    win.geometry("500x500")
    win.configure(bg="#ffffff")

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    distribuicao.plot.pie(
        ax=ax,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"],
        labels=distribuicao.index,
    )
    ax.set_title("Distribuição de Renda (Faixas de Renda)")
    ax.set_ylabel("")

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def grafico_barras_imc_por_renda():
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    win = tk.Toplevel(janela)
    win.title("Barras Empilhadas: IMC por Faixa de Renda")
    win.geometry("650x500")
    win.configure(bg="#ffffff")

    agrupamento = df.groupby(["rendaFamiliar", "imc"]).size().unstack(fill_value=0).sort_index()

    fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
    agrupamento.plot(
        ax=ax,
        kind="bar",
        stacked=True,
        color=["#99ff99", "#66b3ff", "#ff9999"],
    )
    ax.set_title("Distribuição de IMC por Faixa de Renda")
    ax.set_xlabel("Faixa de Renda")
    ax.set_ylabel("Contagem")
    ax.legend(title="IMC", labels=["IMC 1", "IMC 2", "IMC 3"])
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def gerar_fila_ordenada():
    if df is None:
        messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
        return

    try:
        df_ordenado = df.sort_values(by="risco", ascending=False)
        caminho_saida = "assets/fila_ordenada.csv"
        df_ordenado.to_csv(caminho_saida, index=False, sep=";")
        messagebox.showinfo("Sucesso", f"Arquivo 'fila_ordenada.csv' salvo em assets/!")
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