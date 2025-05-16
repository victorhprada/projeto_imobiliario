import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect, text # Added text import

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/clientes_banco.csv'

dados = pd.read_csv(url, sep=',')
print(dados.head())

dados.to_sql('clientes', engine, index=False)

inspector = inspect(engine)
print(inspector.get_table_names())

query = 'SELECT * FROM clientes \
        WHERE Categoria_de_renda="Empregado"'

empregrados = pd.read_sql(query, engine)
print(empregrados)

empregrados.to_sql('empregados', con=engine, index=False)
print(pd.read_sql_table('empregados', engine))

print(pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual']))

query = text('DELETE FROM clientes WHERE ID_Cliente=5008804')
with engine.connect() as conn:
    conn.execute(query)
    conn.commit()  # Added commit to save changes

print(pd.read_sql_table('clientes', engine))