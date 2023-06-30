#Explicações: para não ficar com linhas muito longas e difíceis de serem visualizadas, separei as frases em "partes". No github, 
##para demonstrar que é um texto usamos a "#", para mostrar que a linha debaixo é a continuação da acima, uso "##" (2 hashtags), 
###com a intenção de sinalizar que aquela é a segunda linha de uma mesma anotação. Quando aquela observação acaba, a hashtag no
####início da frase seguinte é apenas uma. Por exemplo, aqui na quarta linha dessa explicação, coloquei quatro hashtags.
#Durante uma das vezes que eu e minhas duas colegas de trabalho nos encontramos para discutir o que iria ser feito,
##decidimos estabelecer uma paleta de cores para cada, que devia ser seguida ao longo de todo o trabalho, para ficar mais 
###harmônico esteticamente. Fizemos a escolha das paletas uma da outra ainda em conjunto, julgando entre si qual era boa 
####e qual não era. A paleta de cores escolhida por mim, e aprovada por minhas colegas, foi: #38375C (Jacarta), #56597C (Purple Navy) 
##### , #787B93 (Rhythm), #F2E6C9 (Champagne), #CAC1B0 (Dark Vanilla) e #AEA49F (Quick Silver). 

import pandas as pd
from bokeh.io import output_file, show, output_notebook
from bokeh.layouts import gridplot
from bokeh.models import Range1d, ColumnDataSource, BasicTicker, ColorBar, FactorRange, LinearColorMapper
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.plotting import figure
from bokeh.transform import factor_cmap, linear_cmap, dodge
from ICdD_modulo_base_para_cds import create_column_data_source

csv_file = "Sleep_Efficiency.csv"
source = create_column_data_source(csv_file)

#GRÁFICO 1
#quis mostrar que quanto maior o consumo de cafeína, menor a ocorrência de um sono profundo
y_range_start = 0 #Colocando o mínimo dos valores do meu y-axis range
y_range_end = 110 #Colocando o máximo dos valores do meu y-axis range

#Criando uma figura com as características atribuídas; 
#"plot_width" e "plot_height" dá as dimensões, "title" coloca o título, 
#"plot.background_fill_color" para colocar a cor de fundo dentro da paleta de cores discutida pelo grupo (escolhi o tom "#38375c")
#"label" para colocar os nomes, e "y_range" especifica os valores do meu "y-axis" (definidos em"y_range_start" e "y_range_end").
p = figure(plot_width=600, plot_height=400, title="Relação entre consumo de cafeína e sono profundo", background_fill_color="#38375c",
           x_axis_label="Sono profundo", y_axis_label="Consumo de cafeina", y_range=(y_range_start, y_range_end))

#Como nossa base de dados é sobre Sleep Efficiency, resolvi colocar estrelas no lugar de pontos no meu scatter plot, combinando mais com a estética do trabalho.
#Olhando passo a passo: "p.star" adiciona estelas ao meu gráfico, "x" e "y" especificam as colunas que devem preencher o gráfico ('Deep sleep percentage' e 'Caffeine consumption'), "size" para definir o tamanho das estrelas, "fill_color" para decidir a tonalidade das estrelas, o tamanho das minhas grid lines estava me incomodando, então usei "p.grid.grid_line_width" para alterar e deixá-las menores, "alpha" para colocar as estrelas levemente transparentes (0.5). 
#OBS.: Usei "line_color" também porque na hora de colocar as estrelas, foi preenchido pela cor escolhida apenas o seu interior, deixando as bordas de outra tonalidade. Como queria a estrela inteira do mesmo tom, usei o fill para ficar completamente "#f2e6c9".
p.star(x=df['Deep sleep percentage'], y=df['Caffeine consumption'], size=14, fill_color='#f2e6c9', line_color='#f2e6c9', alpha=0.5)

p.grid.grid_line_width = 1

output_notebook()
show(p)

#GRÁFICO 2
#possibilita visualizar a quantidade de vezes que as pessoas acordaram, dividido por idade; é possível ver que diversas pessoas 
##com quase 40 anos relataram acordar uma vez por noite, assim como as de quase 60 também e, algumas entre 20 e 30 disseram
###acordar 4 vezes por noite.

#importa a biblioteca matplotlib.pyplot e associa ao nome "plt", pra que eu possa acessar suas funções depois 
import matplotlib.pyplot as plt

#separando e armazenando em variáveis separadas as colunas que vou usar no gráfico;
#"awakenings", com as informações de quantas vezes a pessoa acordou por noite
#"age", com as idades das pessoas
awakenings = df['Awakenings']
age = df['Age']

#Criando o gráfico de disperção hexbin;
#"age" (idade): os valores a serem plotados no eixo x
#"awakenings" (vezes que acordou durante o sono): os valores que devem ser colocados no eixo y
#gridsize: tamanho da grade do hexágono
#cmap: o mapa de cores que deve ser usado. Escolhi o mapa de cores "BuPu"; entrei no site 
##do matplotlib e olhei na aba "Choosing colormaps in Matplotlib" alguns exemplos dos diversos color maps que ele oferece;
###em "Lightness of Matplotlib colormaps" encontrei um color map que se aproximava da paleta de cores que eu deveria seguir  
#### ao longo do trabalho, o "BuPu"
#mincnt: dá número mínimo de pontos necessários para exibir um hexágono. Achei desnecessário colocar todas as colunas
##de hexágonos quando, na verdade, só iriam aparecer 5 colunas; ninguém acordou "Três vezes e meia por noite", "5,2 vezes"... todos 
### os números são inteiros, fazendo com que as linhas do Y (Awakenings) que representam números "quebrados" sejam vazias. 
####Por serem vazias, resolvi as tirar e pedir pela exibição apenas das linhas que haviam dados do Sleep Data.
# edgecolors: decide a cor das bordas dos hexágonos.
plt.hexbin(age, awakenings, gridsize=20, cmap='YlOrBr', mincnt=1, edgecolors='#38375C')
#Essas linhas configuram os rótulos dos eixos x e y para "Idade" (Idade) e "Vezes que acordou", respectivamente
plt.xlabel('Idade')
plt.ylabel('Vezes que acordou')
#Adiciona a exibição barra de cores escolhida e coloca a legenda
plt.colorbar(label='Contagens')
#Coloca o tútulo no gráfico
plt.title('Hexbin Plot: Vezes que acordou por idade')
#exibe o gráfico
plt.show()

#Porém, caso o senhor queira ver meu HexbinPlot com todos os hexágonos e não apenas nas linhas que possuem respostas, aqui está
## o código sem "mincnt".
import matplotlib.pyplot as plt

awakenings = df['Awakenings']
age = df['Age']

plt.hexbin(age, awakenings, gridsize=20, cmap='BuPu', edgecolors='#38375C')

plt.xlabel('Idade')
plt.ylabel('Vezes que despertou')

plt.colorbar(label='Contagens')

plt.title('Hexbin Plot: Vezes que acordou por idade')

plt.show()


#GRÁFICO 3
#No gráfico é possível ver que pessoas fumantes tiveram uma porcentagem maior de REM sleep que os não fumantes, 
#O que é REM Sleep? Rapid eye movement (REM) sleep é um estágio do sono em que a maior parte dos sonhos acontece. Li
##um pouco sobre o assunto e aprendi que esse nome vêm da forma que os nossos olhos se movem enquanto estamos sonhando.

# Agrupa os dados pelo estado do fumante e obtém os valores do REM sleep percentage dele
smoking_groups = df.groupby('Smoking status')['REM sleep percentage'].apply(list)
#Aqui eu criei o boxplot com os dados de porcentagem do REM sleep agrupados por fumante (que era classificado por 
### respostas de "No" e "Yes"). 
#labels: define os rótulos do eixo x, "Yes" e "No"
# patch_artist=True: permite que eu personalize a aparência do boxplot.
bp = plt.boxplot(smoking_groups, labels=['No', 'Yes'], patch_artist=True)

#criei as variáveis que armazenariam as cores do gráfico
background_color = '#F2E6C9' #defini a cor de fundo do gráfico
border_color = '#CAC1B0' #escolhi a cor da borda do gráfico
mean_line_color = '#38375C' #selecionei a cor da linha de mediana
fill_color = '#787B93' #decidi a cor que iria preencher o boxplot

#Coloca a cor de fundo do gráfico
plt.gca().set_facecolor(background_color)

#Bota a cor das bordas do boxplot
for box in bp['boxes']:
    box.set(color=border_color)
    
#Põe a cor da linha de mediana
for median in bp['medians']:
    median.set(color=mean_line_color)
    
#Define o preenchimento dos boxplots
for box in bp['boxes']:
    box.set(facecolor=fill_color)

#Define os rótulos de x e y
plt.xlabel('Smoking Status')
plt.ylabel('REM Sleep Percentage')

#Estabelece o título do gráfico
plt.title('Relação entre Smoking Status e REM Sleep Percentage')

# Exibe o gráfico
plt.show()

