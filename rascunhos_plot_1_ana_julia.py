from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d, HoverTool
from bokeh.io import output_file
from bokeh.transform import factor_cmap
import pandas as pd
from base_limpa import df
from ICdD_modulo_base_para_cds import create_column_data_source

csv_file = "Sleep_Efficiency_Limpa.csv"
source = create_column_data_source(csv_file)

# A ideia inicial é plotar um gráfico comparando a frequência de exercício físico com a média de duração do sono.
# Além disso, resolvi analisar a quantidade de vezes que uma pessoa acorda no meio da noite em meio a tudo isso, sendo o raio do glifo.

# Atribuindo o nome das colunas a variáveis porque acredito que o código fica mais legível
coluna_exercise = "Exercise frequency"
coluna_sleep_duration = "Sleep duration"
coluna_awakenings = "Awakenings"

# Calcula a média da duração do sono de acordo com a frequência de exercícios físicos
mean_sleep_duration = df.groupby(coluna_exercise)[coluna_sleep_duration].mean()
# print(mean_sleep_duration)

# Obtendo uma lista dos valores da média de duração do sono conforme a frequência de exercícios físicos. Serão usados para o eixo y.
valores_media_sleep_duration = []
for valor in mean_sleep_duration:
    valores_media_sleep_duration.append(valor)
# print(valores_media_sleep_duration)

# Obtendo uma lista com os valores únicos da frequência de exercícios físicos. Serão usados para o eixo x.
valores_unicos_exercise = pd.unique(df[coluna_exercise]).tolist()
# print(valores_unicos_exercise)

# média de vezes que as pessoas acordam durante a noite de acordo com a frequencia que praticam exercícios físicos.
mean_awakening_for_exercise_frequency = df.groupby(coluna_exercise)[coluna_awakenings].mean()

# Criar o gráfico com seu título, largura, altura e nome dos eixos.
p = figure(title="Relação entre duração do sono e frequência de exercício físico",
           x_axis_label= "Exercise Frequency",
           y_axis_label= "Average Sleep Duration",
           width=800, height=600)

# Alterando a fonte, a cor e o tamanho da fonte do título
p.title.text_font = "Times New Roman"
p.title.text_color = "#4C2D59"
p.title.text_font_size = "18pt"

# Alterando a fonte, a cor e o tamanho da fonte dos rótulos dos eixos
p.xaxis.axis_label_text_font = "Helvetica"
p.xaxis.axis_label_text_color = "#4C2D59"
p.xaxis.axis_label_text_font_size = "12pt"

p.yaxis.axis_label_text_font = "Helvetica"
p.yaxis.axis_label_text_color = "#4C2D59"
p.yaxis.axis_label_text_font_size = "12pt"

# Definindo o HoverTool. Isso é uma ferramenta do Bokeh que permite mostrar informações interativas no gráfico à medida que o leitor passa o mouse sobre o glifo.
hover = HoverTool(tooltips=[
    ("Exercise frequency", "@x"),
    ("Average Sleep duration", "@y"),
])

# adicionando os glifos que representam a média da duração do sono para cada valor de x. Aqui já está incluída a estética do hover, como a cor.
circle = p.circle(
    valores_unicos_exercise,
    valores_media_sleep_duration,
    line_color="#784A8C",
    fill_color="#784A8C",
    alpha = 1,
    size=mean_awakening_for_exercise_frequency*40,
    legend_label = "awakenings, exercise frequency and sleep durantion",
    hover_fill_color="#C373D9",
    hover_alpha=1,
    hover_line_color="#C373D9")

# Definindo os intervalos dos eixos. Atribuí a variáveis primeiro com o intuito de deixar mais legível.
x_range = Range1d(start=-1, end=6)
y_range = Range1d(start=0, end=12)
p.x_range = x_range
p.y_range = y_range

# Adicionando uma imagem como plano de fundo. O objetivo disso é reforçar o tema do gráfico ao mesmo tempo que favorece a estética.
# Atribuindo algumas informações à variáveis primeiro
background_image_url = '..\imagem_sono_exercicio_fisico.png'
background_opacity = 0.12
# Plotando a imagem de fundo, definindo seu tamanho e a profundiade da sua cor no gráfico.
p.image_url(url=[background_image_url], x=-1, y=0, w=7, h=12, anchor="bottom_left", alpha=background_opacity)

# Adiciona o HoverTool ao gráfico
p.add_tools(hover)

# Definindo o nome do arquivo a ser exibido com o conteúdo do gráfico.
output_file("plot_1_Ana.html", title="plot_1_Ana")

# Exibir o gráfico
show(p)
