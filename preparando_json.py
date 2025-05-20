import pandas as pd
import requests
import json
import numpy as np


url_infor_moveis = 'https://cdn3.gnarususercontent.com.br/2928-transformacao-manipulacao-dados/dados_hospedagem.json'

# Headers para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Fazendo a requisição com headers
    response = requests.get(url_infor_moveis, headers=headers)
    response.raise_for_status()  # Levanta uma exceção para erros HTTP
    
    # Convertendo a resposta para JSON
    data = response.json()
    
    # Criando o DataFrame
    df = pd.DataFrame(data)
    print("Dados carregados com sucesso!")
    print("\nPrimeiras linhas do DataFrame:")
    print(df.head())
    
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")


df = pd.json_normalize(df['info_moveis'])
print(df)

colunas = list(df.columns)
print(colunas)

df = df.explode(column=colunas[3:])
print(df)

df.reset_index(inplace=True, drop=True) # Resetando o index
print(df)

print(df.info())

# Limpando os dados antes da conversão
limpar_valor = lambda x: float(str(x).replace('$', '').replace(',', '')) if not pd.isna(x) else np.nan

# Tratando dados com numpy, convertendo dados
col_numericas = ['quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas', 'max_hospedes']
df[col_numericas] = df[col_numericas].astype('Int64')

col_float = ['avaliacao_geral', 'taxa_limpeza', 'preco', 'taxa_deposito']
# Limpando e convertendo as colunas float de uma vez
df[col_float] = df[col_float].applymap(limpar_valor)

print("\nInformações do DataFrame após conversão:")
print(df.info())

# Exibindo algumas estatísticas básicas
print("\nEstatísticas descritivas das colunas numéricas:")
print(df[col_float].describe())

print(df[['taxa_deposito', 'taxa_limpeza']])

print(df['descricao_local'])
df['descricao_local'] = df['descricao_local'].str.lower()
print(df['descricao_local'])

print(df['descricao_local'][3169]) # Buscando um valor especifico dentro da coluna

# Limpando a descrição do local
# Remove caracteres especiais mantendo letras, números, hífen e apóstrofo
df['descricao_local'] = df['descricao_local'].str.replace(r'[^a-zA-Z0-9\-\'\s]', ' ', regex=True)
# Remove hífens soltos (que não estão entre palavras)
df['descricao_local'] = df['descricao_local'].str.replace(r'\s*-\s*', ' ', regex=True)
# Remove espaços múltiplos
df['descricao_local'] = df['descricao_local'].str.replace(r'\s+', ' ', regex=True)
# Remove espaços no início e fim
df['descricao_local'] = df['descricao_local'].str.strip()

print("\nDescrição do local após limpeza:")
print(df['descricao_local'][3169])

print("\nPalavras separadas:")
print(df['descricao_local'].str.split())

df['descricao_local'] = df['descricao_local'].str.split()
print(df.head())

df['comodidades'] = df['comodidades'].str.replace(r'\{|\}|\"', '', regex=True) #Tokenizando
df['comodidades'] = df['comodidades'].str.split(',')
print(df['comodidades'])

data_url = 'https://cdn3.gnarususercontent.com.br/2928-transformacao-manipulacao-dados/moveis_disponiveis.json'
try:
    response = requests.get(data_url, headers=headers)
    response.raise_for_status()
    dt_data = pd.DataFrame(response.json())
    print(dt_data.head())
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")

print(dt_data.info())
dt_data['data'] = pd.to_datetime(dt_data['data'])
print(dt_data.info())

# Group by year-month before converting to string
df_agrupado = dt_data.groupby(dt_data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
print(df_agrupado)

# Convert to string format after grouping
dt_data['data'] = dt_data['data'].dt.strftime('%Y-%m')
print(dt_data.head())