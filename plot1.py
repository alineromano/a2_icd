from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from base_limpa import df

# gráfico de barras Awakenings x Deep sleep percentage

# cria um dataframe em que uma coluna são as opções de awakenings e a outra são as % de deep sleep para cada uma dessas opções
media_deep_awake = df.groupby('Awakenings')['Deep sleep percentage'].mean().reset_index() # esse cógigo agrupa o df por Awakenings e faz a média de deep sleep, depois transforma em um df

# transforma as opções de awakenings em string
media_deep_awake['Awakenings'] = media_deep_awake['Awakenings'].astype(str) 

# definindo o column data source para plotar os gráficos
source = ColumnDataSource(media_deep_awake)


plot = figure(x_range=media_deep_awake['Awakenings'].tolist())


plot.vbar(x='Awakenings', top='Deep sleep percentage', width=0.5, source=source,
          fill_color=factor_cmap('Awakenings', palette=['blue', 'pink', 'orange', 'red', 'green'], factors=media_deep_awake['Awakenings'].tolist()))


plot.xaxis.axis_label = "Awakenings"
plot.yaxis.axis_label = "Average Deep Sleep Percentage"

show(plot)
