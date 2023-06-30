from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
from base_limpa import df

# gráfico de barras Awakenings x Light, Deep  e REM sleep percentage
# Dessa forma, é possível analisar como é o ciclo do sono é dividido dependendo da quantidade de vezes que a pessoa acorda durante a noite

def create_plot1():

       # definindo as categorias
       awakenings = df['Awakenings'].unique().astype(str).tolist() # lista os valores únicos de Awakenings
       awakenings.sort() # ordem crescente
       sleep_categories = ['Light sleep percentage', 'Deep sleep percentage', 'REM sleep percentage'] # as 3 % do sono que serão analisadas

       # define o data como um dicionário de awakenings
       data = {'awakenings': awakenings}

       # para cada categoria de sleep, adiciona uma lista com as médias da % em cada opção de awakenings (0, 1 ,2, 3 e 4)
       for category in sleep_categories:
              media_por_awake = df[category].groupby(df['Awakenings']).mean() # cria uma série as médias da % para awakenings
              data[category] = media_por_awake.tolist() # transforma em lista e adiciona como valor para chave da categoria

       # define o column data source para o gráfico
       source = ColumnDataSource(data = data)

       # cria a figura, define intervalo de x, y e as ferramentas de interação
       plot = figure(x_range=awakenings, y_range=(0, 100), tools="pan,wheel_zoom,box_select,box_zoom,reset,save")

       # monta as barras para Light sleep
       plot.vbar(x=dodge('awakenings', -0.25, range=plot.x_range), top='Light sleep percentage', source=source,
              width=0.2, color="#c9d9d3", legend_label="Light sleep percentage")

       # monta as barras para Deep sleep
       plot.vbar(x=dodge('awakenings',  0.0,  range=plot.x_range), top='Deep sleep percentage', source=source,
              width=0.2, color="#718dbf", legend_label="Deep sleep percentage")

       # monta as barras para REM sleep
       plot.vbar(x=dodge('awakenings',  0.25, range=plot.x_range), top='REM sleep percentage', source=source,
              width=0.2, color="#e84d60", legend_label="REM sleep percentage")

       # título
       plot.title="Sleep cicle % by Awakenings"

       # estéticas
       plot.height=350 #altura
       plot.x_range.range_padding = 0.1 # borda
       plot.xgrid.grid_line_color = None # tira os grids verticais

       # legenda
       plot.legend.location = "top_left"
       plot.legend.orientation = "horizontal"

       #show(plot)

       return plot
