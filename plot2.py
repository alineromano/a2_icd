#Explicações: para não ficar com linhas muito longas e difíceis de serem visualizadas, separei as frases em "partes". No github, 
##para demonstrar que é um texto usamos a "#", para mostrar que a linha debaixo é a continuação da acima, uso "##" (2 hashtags), 
###com a intenção de sinalizar que aquela é a segunda linha de uma mesma anotação. Quando aquela observação acaba, a hashtag no
####início da frase seguinte é apenas uma. Por exemplo, aqui na quarta linha dessa explicação, coloquei quatro hashtags.

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

#Como nossa base de dados é sobre Sleep Efficiency, resolvi colocar estrelas no lugar de pontos no meu scatter plot, combinando
##mais com a estética do trabalho.
#"p.star" adiciona estelas ao meu gráfico 
#"x" e "y" especificam as colunas que devem preencher o gráfico ('Deep sleep percentage' e 'Caffeine consumption')
#"size" para definir o tamanho das estrelas
#"fill_color" para decidir a tonalidade das estrelas
#o tamanho das grid lines estava me incomodando, então usei "p.grid.grid_line_width" para alterar e deixá-las menores
#"alpha" para colocar as estrelas levemente transparentes (0.5). 
#OBS.: Usei "line_color" também porque na hora de colocar as estrelas, foi preenchido pela cor escolhida apenas o seu interior,
##deixando as bordas de outra tonalidade. Como queria a estrela inteira do mesmo tom, usei o fill para ficar completamente "#f2e6c9".
p.star(x=df['Deep sleep percentage'], y=df['Caffeine consumption'], size=14, fill_color='#f2e6c9', line_color='#f2e6c9', alpha=0.5)

p.grid.grid_line_width = 1

output_notebook()
show(p)

#GRÁFICO 2
#Gráfico de barras com a relação entre Smoking Status e eficiência do sono, é possível notar que pessoas não fumantes
##obtiveram uma eficiência maior que as fumantes durante o sono
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

#Dados de cada uma das colunas (smoking_status com as respostas sendo de "Yes" ou "No", por exemplo)
smoking_status = ['Yes', 'No']
sleep_efficiency = [85, 92]

# Criando o ColumnDataSource com os dados
source = ColumnDataSource(data=dict(smoking_status=smoking_status, sleep_efficiency=sleep_efficiency))

p = figure(x_range=smoking_status, plot_height=400, title='Relação entre Smoking Status e Sleep Efficiency',
           x_axis_label='Smoking Status', y_axis_label='Sleep Efficiency',
           background_fill_color="#AEA49F")
#x_range: dá o range do meu x, que no caso é Smoking Status (uma lista de "Sim" e "Não")
#plot_height: especifica a altura do plot
# title: coloca o título no gráfico, no caso foi 'Relação entre Smoking Status e Sleep Efficiency'
#x_axis_label: coloca o nome da minha x-axis (Smoking Status)
#y_axis_label: põe o nome da minha y-axis (Sleep Efficiency)
#background_fill_color: determina a cor de fundo do gráfico, "#AEA49F" (dentro da paleta de cores selecionada)

# Plotar as barras;
#x: especifica o que está na minha linha vertical (Smoking Status)
#width: dá a largura das minhas barras 
#fill_color: coloca a cor que preencherá as minhas barras, nesse caso "#38375C", que está dentro da paleta de cores.
#line_color: coloca a cor das bordas das minhas barras, no caso é preto (black)
#alpha: ajusta a transparência das barras 
#source: especifica a fonte dos meus dados para o gráfico  
p.vbar(x='smoking_status', top='sleep_efficiency', width=0.5, fill_color="#38375C", line_color='black', alpha=0.7, source=source)

#text_font_size: coloca o tamanho de fonte desejado nas minhas palavras
p.title.text_font_size = '14pt'
p.xaxis.axis_label_text_font_size = '12pt'
p.yaxis.axis_label_text_font_size = '12pt'

output_notebook()
show(p) #exibe o gráfico

#GRÁFICO 3 
#gráfico de dispersão com a relação entre Awakenings por Idade, é possível notar que dos 20 aos 30 e dos 40 aos 50 foram as pessoas de
##faixa etária que mais relataram acordar quatro vezes, enquanto, de um modo geral, a maioria disse ter acordado apenas uma vez.
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource

source = ColumnDataSource(df) #cria um columndatasource com os dados

#plot_width: define a largura da figura
#plot_height: coloca a altura da figura
#title: coloca o título no gráfico
#background_fill_color: bota a cor de fundo no gráfico (dentro da paleta de cores)
p = figure(plot_width=600, plot_height=400, title='Relação entre Awakenings e Age',
           x_axis_label='Age', y_axis_label='Awakenings', 
           background_fill_color='#787B93')

#Plotando as estrelas;
#fill_color: a cor que as desejo, dentro da paleta de cores selecionada
#line_color=None, porque não desejava que suas linhas possuíssem uma cor, removendo-as
#angle: ângulo que desejo que a estrela esteja
#size: tamanho que a estrela deve ter
p.star(x='Age', y='Awakenings', size=12, angle=-1.2, fill_color='#38375C', line_color=None, source=source)

#Adicionando informações para o rótulo e o título;
#title.text_font_size: coloca o tamanho da fonte do título
#xaxis.axis_label_text_font_size: coloca o tamanho da fonte do texto em x
#yaxis.axis_label_text_font_size: coloca o tamanho da fonte do texto em y
p.title.text_font_size = '14pt'
p.xaxis.axis_label_text_font_size = '12pt'
p.yaxis.axis_label_text_font_size = '12pt'

output_notebook()
show(p)
