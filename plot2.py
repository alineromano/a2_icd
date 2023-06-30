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
