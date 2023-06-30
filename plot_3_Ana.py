from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d, HoverTool
from bokeh.io import output_file
import pandas as pd
import numpy as np
from base_limpa import df
from ICdD_modulo_base_para_cds import create_column_data_source


def create_plot9():
    cvs_file = "Sleep_Efficiency_Limpa.csv"
    source = create_column_data_source(cvs_file)

    # A ideia dessas análises agora é comparar idade com a porcentagem de sono REM.
    # O sono REM é uma etapa do sono na qual costumamos sonhar, as ondas cerebrais ficam ativas e a respiração e batimentos acelerados. 
    # Mas, os músculos permanecem paralisados.

    # Atribuindo o nome das colunas que serão usadas a variáveis com o intuito de deixar o código mais legível.
    coluna_idade = "Age"
    coluna_porcentagem_sono_REM = "REM sleep percentage"

    p = figure(title="Porcentagem Sono REM por idade",
            x_axis_label= "Idade",
            y_axis_label= "Porcentagem Sono REM",
            width=800, height=600)

    # Alterando a fonte, a cor e o tamanho da fonte do título
    p.title.text_font = "Times New Roman"
    p.title.text_color = "#A68780"
    p.title.text_font_size = "20pt"

    # Alterando a fonte, a cor e o tamanho da fonte dos rótulos dos eixos
    p.xaxis.axis_label_text_font = "Helvetica"
    p.xaxis.axis_label_text_color = "#4C2D59"
    p.xaxis.axis_label_text_font_size = "12pt"

    p.yaxis.axis_label_text_font = "Helvetica"
    p.yaxis.axis_label_text_color = "#4C2D59"
    p.yaxis.axis_label_text_font_size = "12pt"

    # Definindo os intervalos dos eixos. Atribuí a variáveis primeiro com o intuito de deixar mais legível.
    x_range = Range1d(start=0, end=80)
    y_range = Range1d(start=0, end=40)
    p.x_range = x_range
    p.y_range = y_range

    # Adicionando um deslocamento aleatório aos pontos para criar o efeito de Gitter
    deslocamento = np.random.uniform(-0.9, 0.9, len(df))
    df[coluna_idade] += deslocamento

    p.asterisk(df[coluna_idade], df[coluna_porcentagem_sono_REM],
            legend_label="Sono REM por idade", fill_color="#784A8C", size=9, alpha=0.6)

    # Adicionando uma imagem como plano de fundo. O objetivo disso é reforçar o tema do gráfico ao mesmo tempo que favorece a estética.
    # Atribuindo algumas informações à variáveis primeiro
    background_image_url = "imagem_sono_REM_teste.png"
    background_opacity = 0.14
    # Plotando a imagem de fundo, definindo seu tamanho e a profundiade da sua cor no gráfico.
    p.image_url(url=[background_image_url], x=0, y=0, w=80, h=40, anchor="bottom_left", alpha=background_opacity)

    # Definindo o nome do arquivo a ser exibido com o conteúdo do gráfico.
    output_file("plot_3_Ana.html", title="plot_3_Ana")

    # Exibir o gráfico
    #show(p)
    return p