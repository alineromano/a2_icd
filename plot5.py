from bokeh.io import show
from bokeh.models import Range1d
from bokeh.models.annotations import BoxAnnotation
from bokeh.plotting import figure
from ICdD_modulo_base_para_cds import create_column_data_source

def create_plot5():

    # definindo o columdatasource
    csv_file  = 'Sleep_Efficiency_Limpa.csv'
    source = create_column_data_source(csv_file)

    # gráfico de dispersão entre deep x light sleep, proporcional a sleep efficiency
    # pelo gráfico, é possível verificar dois grupos distintos, destacados pelo box annotation

    # criando a figure
    plot = figure()

    # cria uma coluna multiplicando sleep efficiency para aumentar o tamanho geral dos pontos no gráfico
    source.data['Sleep efficiency multiplicado'] = source.data['Sleep efficiency'] * 15

    # criando o gráfico de dispersão (em formato de estrela)
    plot.star(x="Deep sleep percentage", y="Light sleep percentage", size = "Sleep efficiency multiplicado" , color ="lightyellow", source = source) 

    # montado as caixas
    box_annotation1 = BoxAnnotation(left = 15, right = 40, top = 65, bottom = 35, line_color = "pink", line_width = 5, fill_color = None, line_alpha = 1)
    plot.add_layout(box_annotation1)

    box_annotation2 = BoxAnnotation(left = 47, right = 78, top = 33, bottom = 5, line_color = "lightblue", line_width = 5, fill_color = None, line_alpha = 1)
    plot.add_layout(box_annotation2)

    # definindo as legendas dos eixos
    plot.xaxis.axis_label = "Deep sleep percentage"
    plot.yaxis.axis_label = "Light sleep percentage"

    # definindo os intervalos dos eixos
    plot.x_range = Range1d(start = 0, end = 80)
    plot.y_range = Range1d(start = 0, end = 70)

    # título
    plot.title="Light x Deep Sleep effects on Sleep Efficiency"

    # estética do fundo
    plot.grid.grid_line_alpha = 0.3
    plot.background_fill_color = "#0D0224"

    #show(plot)

    return plot