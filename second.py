import pandas as pd

arq = '/Users/victorhugopradateixeira/Projeto Mercado/emissoes_CO2.xlsx'

df = pd.read_excel(arq)
print(df.head())

# Visualizando as planilhas dentro de um mesmo aquivo
df = pd.ExcelFile(arq).sheet_names
print(df)

df_emissoes_CO2 = pd.read_excel(arq, sheet_name='emissoes_C02')
print(df_emissoes_CO2.head())
# Captando o intervalo dentro da planilha de emissoes_CO2
intervalo = pd.read_excel(arq, sheet_name='emissoes_C02', usecols='A:D', nrows=10)
print(intervalo.head())

df_emissoes_percapita = pd.read_excel(arq, sheet_name='emissoes_percapita')
print(df_emissoes_percapita.head())

df_fontes = pd.read_excel(arq, sheet_name='fontes')
print(df_fontes.head())

# Escrevendo arquivos no Excel
#df_emissoes_percapita.to_excel('co2_percapita.xlsx', index=False)

arq_percapita = '/Users/victorhugopradateixeira/Projeto Mercado/co2_percapita.xlsx'
df_emissoes_percapita_new = pd.read_excel(arq_percapita)
print(df_emissoes_percapita_new)