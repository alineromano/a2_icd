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
#print(awakenings_count)

media_efic_awakenings = df['Sleep efficiency'].groupby(df['Awakenings']).mean() # calculando a média de eficiência para cada número
#print(media_efic_awakenings)

# é possível observar que pessoas que acordam 0 ou 1 vez tem eficiência do sono maior do que as demais

# análise de light, deep e REM %
soma_porcentagens = df['Light sleep percentage'][9] + df['Deep sleep percentage'][9] + df['REM sleep percentage'][9]
print(soma_porcentagens)

# essas 3 % representam as 3 fases do ciclo do sono
# a soma das  porcentagens é de 100%. ou seja, ao aumentar uma porcentagem, outra deve diminuir para que elas sempre somem 100%.

media_light = df['Light sleep percentage'].mean()
media_deep = df['Deep sleep percentage'].mean()
media_rem = df['REM sleep percentage'].mean()
print(media_light, media_deep, media_rem)

# em média, o sono deep é o maior, reprentando quase 50%
# light e rem tem médias semelhantes
# ideia: estudar essas % em relação a Awakenings
