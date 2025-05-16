import pandas as pd

url =  'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/superstore_data.csv'

df = pd.read_csv(url, sep=',')

print(df.head())

dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])
print(dados_selecao)

dados_selecao.to_csv('clientes_mercado.csv', index=False, sep=';')
dados_selecao_new = pd.read_csv('/Users/victorhugopradateixeira/Projeto Mercado/clientes_mercado.csv', sep=';')
print(dados_selecao_new.head())

