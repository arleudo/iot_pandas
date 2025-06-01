import pandas as pd
import matplotlib.pyplot as plt

imc = 1
refluxoGastroesofagico = 1
asma = 1
pancreatite = 1
incontinenciaUrinariaDeEsforco = 1
colelitíase = 1
disfuncaoEretil = 1
sindromeDoOvarioPolicistico = 1
varizes = 1
hipertensaoIntracranianaIdiopatica = 1
depressao = 1
esteatoseHepatica = 2
herniaDeDisco = 2
dislipidemia = 2
apneiaDoSono = 2
infertilidade = 2
ansiedade = 3
doencasCardiovasculares = 3
historicoTromboembolismo = 3
diabetesTipoII = 3
osteoartriteIncapacitante = 3

def calcular_risco(row):
    fatorIdade = row['idade']
    if fatorIdade < 18:
        fatorIdade = 1
    elif fatorIdade < 40:
        fatorIdade = 2
    else:
        fatorIdade = 3
    
    fatorRenda = row['rendaFamiliar']
    if fatorRenda == 1:
        fatorRenda = 5
    elif fatorRenda == 2:
        fatorRenda = 4
    elif fatorRenda == 3:
        fatorRenda = 3
    elif fatorRenda == 4:   
        fatorRenda = 2
    elif fatorRenda == 5:
        fatorRenda = 1

    return (
        row['imc'] * imc
        + fatorIdade
        + fatorRenda
        + row['refluxoGastroesofagico'] * refluxoGastroesofagico
        + row['asma'] * asma
        + row['pancreatite'] * pancreatite
        + row['incontinenciaUrinariaDeEsforco'] * incontinenciaUrinariaDeEsforco
        + row['colelitíase'] * colelitíase
        + row['disfuncaoEretil'] * disfuncaoEretil
        + row['sindromeDoOvarioPolicistico'] * sindromeDoOvarioPolicistico
        + row['varizes'] * varizes
        + row['hipertensaoIntracranianaIdiopatica'] * hipertensaoIntracranianaIdiopatica
        + row['depressao'] * depressao
        + row['esteatoseHepatica'] * esteatoseHepatica
        + row['herniaDeDisco'] * herniaDeDisco
        + row['dislipidemia'] * dislipidemia
        + row['apneiaDoSono'] * apneiaDoSono
        + row['infertilidade'] * infertilidade
        + row['ansiedade'] * ansiedade
        + row['doencasCardiovasculares'] * doencasCardiovasculares
        + row['historicoTromboembolismo'] * historicoTromboembolismo
        + row['diabetesTipoII'] * diabetesTipoII
        + row['osteoartriteIncapacitante'] * osteoartriteIncapacitante
    )

def ler_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo, sep=';')
        
        df['risco'] = df.apply(calcular_risco, axis=1)
        print(df.head(10))

        gerar_grafico_pizza(df)
        gerar_grafico_barras_empilhadas(df)

        df_ordenado = df.sort_values(by='risco', ascending=False)
        df_ordenado.to_csv('assets/fila_ordenada.csv', index=False, sep=';')

        print("\nArquivo 'fila.csv' salvo com sucesso no diretório atual.")

        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

def gerar_grafico_barras_empilhadas(df):
    agrupamento = df.groupby(['rendaFamiliar', 'imc']).size().unstack(fill_value=0)

    agrupamento.plot(
        kind='bar',
        stacked=True,        
        figsize=(10, 6),
        color=['#99ff99', '#66b3ff', '#ff9999'],
    )
    plt.title('Distribuição de IMC por Faixa de Renda')
    plt.xlabel('Faixa de Renda')
    plt.ylabel('Contagem')
    plt.legend(title='IMC', labels=['IMC 1', 'IMC 2', 'IMC 3'])
    plt.show()

def gerar_grafico_pizza(df):
    faixas_etarias = pd.cut(
        df['idade'], bins=[0, 18, 40, 60, 80], labels=['0-18', '19-40', '41-60', '61-80']
    )
    distribuicao = faixas_etarias.value_counts()

    plt.figure(figsize=(8, 8))
    distribuicao.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.title('Distribuição de Idades (Faixas Etárias)')
    plt.ylabel('')
    plt.show()

    faixas_risco = pd.cut(
        df['risco'], bins=[0, 15, 20, 25, 30], labels=['0-15', '16-20', '21-25', '26-30']
    )
    distribuicao_risco = faixas_risco.value_counts()

    plt.figure(figsize=(8, 8))
    distribuicao_risco.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.title('Distribuição de Risco (Faixas Riscos)')
    plt.ylabel('')
    plt.show()

    faixas_renda = pd.cut(
        df['rendaFamiliar'], 
        bins=[0, 1, 2, 3, 4, 5], 
        labels=[
            'Até 1 salário mínimo', 
            'Até 2 salários mínimos', 
            'Até 3 salários mínimos', 
            'Até 4 salários mínimos', 
            '5 salários mínimos ou mais'
        ]
    )
    distribuicao_renda = faixas_renda.value_counts()

    plt.figure(figsize=(8, 8))
    distribuicao_renda.plot.pie(
        autopct='%1.1f%%',
        startangle=90,
        colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    )
    plt.title('Distribuição de Renda (Faixas de Renda)')
    plt.ylabel('')
    plt.show()

caminho_arquivo = "assets/dados.csv"

if __name__ == "__main__":
    caminho_arquivo = "assets/dados.csv"
    ler_csv(caminho_arquivo)