
import pandas as pd

# ler a tabela renda.csv
renda = pd.read_csv("renda.csv")

# ler a tabela populacao.csv
populacao = pd.read_csv("populacao.csv")

# unir as tabelas por "estado"
relatorio = pd.merge(renda, populacao, on="estado")

# reordenar as colunas
relatorio = relatorio[["id_x", "pais", "estado","populacao", "media_de_renda"]]

# renomear a coluna id_x para id
relatorio = relatorio.rename(columns={"id_x": "id"})

# salvar o novo relatório em um arquivo csv
relatorio.to_csv("relatorio_unido.csv", index=False)



