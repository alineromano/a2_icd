from base_limpa import df #importando a base limpa
import pandas as pd

pd.set_option('display.max_rows', None) # mostar todas as linhas
pd.set_option('display.max_columns', None)

#df.info() # analisando tipo e quantidade das variáveis

describe = df.describe() # analisando variáveis quanti
#print(describe)

sample = df.sample(5) # amostra da base
#print(sample)

# a princípio, são 10 variáveis quanti e 4 quali, 
# porém algumas variáveis quantis apresentam poucas opções de respostas e poderiam ser tratadas como quali também.
# ex: Awakenings tem 5 opções: 0, 1, 2, 3 ou 4. Dessa forma, poderia ser tradada como uma coluna com 5 categorias.
# ideia: fazer um gráfico de barras relacionando Awakenings a alguma coluna quanti, como Sleep efficiency

awakenings_count = df['Awakenings'].value_counts() # contando a ocorrência de cada número
print(awakenings_count)

media_efic_awakenings = df['Sleep efficiency'].groupby(df['Awakenings']).mean() # calculando a média de eficiência para cada número
print(media_efic_awakenings)

# é possível observar que pessoas que acordam 0 ou 1 vez tem eficiência do sono maior do que as demais