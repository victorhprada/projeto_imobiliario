import pandas as pd

url_json_pacientes = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/pacientes.json'

df_pacientes = pd.read_json(url_json_pacientes)
print(df_pacientes)

url_json_pacientes_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/pacientes_2.json'

df_pacientes_2 = pd.read_json(url_json_pacientes_2)
print(df_pacientes_2)

# Normalizando os dados do Json
df_pacientes_2_normalizado = pd.json_normalize(df_pacientes_2['Pacientes'])
print(df_pacientes_2_normalizado)

# Salvar o arquivo normalizado
df_pacientes_2_normalizado.to_json('historico_pacientes_normalizado.json')
