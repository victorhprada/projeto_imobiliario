import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'


dados = pd.read_csv(url, sep=';')

print(dados)

print(dados.head())
print(dados.tail())
print(type(dados))
print(dados.shape)
print(dados.columns)
print(dados.info())

print(dados['Tipo'])

## Valor médio dos valores dos imovéis
print(dados['Valor'].mean())

## Valor médio dos valores dos imovéis agrupados por tipo
print(dados.groupby('Tipo').mean(numeric_only=True))

## Valor médio do valor dos imovéis agrupados por tipo
print(dados.groupby('Tipo')['Valor'].mean())

## Adicionando dentro de um DataFrame
df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values(by='Valor')
print(df_preco_tipo)

fig = df_preco_tipo.plot(kind='barh', figsize=(18, 5), color='green')
#plt.show()

## Pegando os dados únicos da tabela de Tipo
print(dados['Tipo'].unique())
imoveis_comerciais = ['Loja/Salão', 'Loja Shopping/ Ct Comercial', 'Conjunto Comercial/Sala', 'Casa Comercial', 'Prédio Inteiro', 'Galpão/Depósito/Armazém', 'Indústria']

df = dados.query('Tipo not in @imoveis_comerciais')
print("\nDataFrame filtrado (primeiras 5 linhas):")
print(df.head())
print("\nTipos únicos no DataFrame filtrado:")
print(df['Tipo'].unique())


# Filtrando imóveis com uma ou mais suítes
imoveis_com_suite = df.query('Suites >= 1')
print("\nImóveis com uma ou mais suítes (primeiras 5 linhas):")
print(imoveis_com_suite.head())
print("\nQuantidade de imóveis com suítes:", len(imoveis_com_suite))

# Média de valor dos imóveis com suítes por tipo
df_preco_tipo = imoveis_com_suite.groupby('Tipo')[['Valor']].mean().sort_values(by='Valor')
fig = df_preco_tipo.plot(kind='barh', figsize=(18, 5), color='purple')
#plt.show()

# Qual o percentual de cada tipo de imóvel na nossa base de dados?
df['Tipo'].unique()
print(df['Tipo'].value_counts(normalize=True))

print(df['Tipo'].value_counts(normalize=True).to_frame().sort_values(by='Tipo'))
df_percentual_tipo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values(by='Tipo')

df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color='blue', xlabel='Tipos', ylabel='Percentual')
#plt.show()

## Apenas imovéis do tipo apartamento
df_tipo_apartamento = df.query('Tipo == "Apartamento"')
print(df_tipo_apartamento)

# Quantidade de dados nulos por coluna
print(df_tipo_apartamento.isnull().sum())

# Substituindo valores nulos
print(df_tipo_apartamento.fillna(0))
df_tipo_apartamento = df_tipo_apartamento.fillna(0)
print(df_tipo_apartamento)
print(df_tipo_apartamento.isnull().sum())

print(df_tipo_apartamento.query('Valor == 0 | Condominio == 0'))
print(df_tipo_apartamento.query('Valor == 0 | Condominio == 0').index)
registros_a_remover = df_tipo_apartamento.query('Valor == 0 | Condominio == 0').index
df_tipo_apartamento.drop(registros_a_remover, axis=0, inplace=True)
print(df_tipo_apartamento.query('Valor == 0 | Condominio == 0'))

print(df_tipo_apartamento.head())
print(df_tipo_apartamento['Tipo'].unique())
df_tipo_apartamento.drop('Tipo', axis=1, inplace=True)
print(df_tipo_apartamento.head())

# Apartamentos que possuem 1 quarto e aluguel menor que 1200
df_apartamento_1quarto = df_tipo_apartamento.query('Quartos == 1 and Valor < 1200')
print(df_apartamento_1quarto.head())

df_tipo_apartamento.to_csv('dados_apartamentos.csv', index=False)
print(pd.read_csv('/Users/victorhugopradateixeira/Projeto Imobiliaria/dados_apartamentos.csv'))