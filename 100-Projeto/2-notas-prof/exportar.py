import sqlite3
import pandas as pd

# Conecta ao banco
conectar = sqlite3.connect("bd.sqlite")

# Lê o resultado da consulta
df = pd.read_sql_query("SELECT * FROM Turma_3A_1B", conectar
)

# Fecha a conexão
conectar.close()

print(df)