import pandas as pd

# lendo a base e salvando como df
df = pd.read_csv("Sleep_Efficiency.csv")

# apagando as linhas com valores vazios
df = df.dropna()

# fazendo tratamento nas colunas
df['Wakeup time'] = pd.to_datetime(df['Wakeup time']).dt.time.astype(str) # deixando somente o horário e mudando para string
df['Bedtime'] = pd.to_datetime(df['Bedtime']).dt.time.astype(str) # deixando somente o horário e mudando para string
df["Awakenings"] = df["Awakenings"].astype(int) # mudando para integer

