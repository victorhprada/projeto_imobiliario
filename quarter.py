import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Evolu%C3%A7%C3%A3o'

df = pd.read_html(url)
print(df)

print(len(df))

url_df_leitura = df[0]
print(url_df_leitura)