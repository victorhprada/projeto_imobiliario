import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados = pd.read_csv(url, sep=';')
print(dados.head())

# Criando colunas numéricas para valores mensais e anuais
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
print(dados.head())

dados['Valor_por_ano'] = (dados['Valor_por_mes'] * 12) + dados['IPTU']
print(dados.head())

# Criando colunas categóricas
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                     dados['Quartos'].astype(str) + ' quarto(s) ' + \
                     ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem. '
print(dados.head())

# Criação de coluna binária
dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
print(dados.head())

dados.to_csv('dados_completos.csv', index=False, sep=';')
dados_completos = pd.read_csv('/Users/victorhugopradateixeira/Projeto Imobiliaria/dados_completos.csv')
print(dados_completos.head())