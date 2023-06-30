from bokeh.plotting import figure, show 
from bokeh.io import output_file
from bokeh.models import Range1d
import pandas as pd
import numpy as np
from base_limpa import df
from ICdD_modulo_base_para_cds import create_column_data_source

csv_file = "Sleep_Efficiency_Limpa.csv"
source = create_column_data_source(csv_file)

# Nessa pasta, quero trabalhar com a relação entre as médias do consumo de alcóol, da porcentagem do sono profundo e do leve.
# Talvez eu analise se a pessoa fuma ou não também. Porque acho que teria correlação com as duas variáveis iniciais.

# Atribuindo o nome das colunas que serão usadas à variáveis com o intuito de deixar o código mais legível
coluna_consumo_alcool = "Alcohol consumption"
coluna_porcentagem_sono_profundo = "Deep sleep percentage"
coluna_porcentagem_sono_leve = "Light sleep percentage"

p = figure(title="Consumo de Álcool e Porcentagem de duração das etapas do Sono",
           x_axis_label= "Consumo de Álcool",
           y_axis_label= "Porcentagens",
           width=800, height=600,
           background_fill_color="#50C4F2",
           background_fill_alpha=0.1)

# Alterando a fonte, a cor e o tamanho da fonte do título
p.title.text_font = "Times New Roman"
p.title.text_color = "#50C4F2"
p.title.text_font_size = "20pt"

# Alterando a fonte, a cor e o tamanho da fonte dos rótulos dos eixos
p.xaxis.axis_label_text_font = "Helvetica"
p.xaxis.axis_label_text_color = "#4C2D59"
p.xaxis.axis_label_text_font_size = "12pt"

p.yaxis.axis_label_text_font = "Helvetica"
p.yaxis.axis_label_text_color = "#4C2D59"
p.yaxis.axis_label_text_font_size = "12pt"

# Definindo os intervalos dos eixos. Atribuí a variáveis primeiro com o intuito de deixar mais legível.
x_range = Range1d(start=-1, end=6)
y_range = Range1d(start=0, end=80)
p.x_range = x_range
p.y_range = y_range

# Adicionando um deslocamento aleatório aos pontos para criar o efeito de Gitter
deslocamento = np.random.uniform(-0.7, 0.7, len(df))
df[coluna_consumo_alcool] += deslocamento

p.asterisk(df[coluna_consumo_alcool], df[coluna_porcentagem_sono_profundo],
          legend_label="Sono Profundo", fill_color="#50C4F2", size=8, alpha=0.6)

p.star(df[coluna_consumo_alcool], df[coluna_porcentagem_sono_leve],
          legend_label="Sono Leve", fill_color="#C373D9", size=10, alpha=1.5)

# Definindo o nome do arquivo a ser exibido com o conteúdo do gráfico.
output_file("plot_2_Ana.html", title="plot_2_Ana")

# Exibir o gráfico
show(p)


