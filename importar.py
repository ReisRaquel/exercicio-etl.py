import pandas as pd
import pyodbc

# Lendo o arquivo CSV usando o método read_csv
df = pd.read_csv("relatorio_unido.csv")

# Criando uma conexão com o SQL Server
conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:dados-sql.database.windows.net,1433;Database=dados-csv;Uid=administradora;Pwd=@Emesson16;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

# Loop através de cada linha no DataFrame
for index, row in df.iterrows():
    # Inserindo uma linha na tabela
    conn.execute("INSERT INTO relatorio_unido ( pais, estado, populacao, media_de_renda) VALUES (?, ?, ?, ?)", row[0], row[1], row[2],row[3])

# Salvando as mudanças
conn.commit()

# Fechando a conexão
conn.close()