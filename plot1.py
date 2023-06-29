from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
from base_limpa import df

# gráfico de barras Awakenings x Light, Deep  e REM sleep percentage
# Dessa forma, é possível analisar como é o ciclo do sono é dividido dependendo da quantidade de vezes que a pessoa acorda durante a noite

awakenings = df['Awakenings'].unique().astype(str).tolist()
awakenings.sort()
categories = ['Light sleep percentage', 'Deep sleep percentage', 'REM sleep percentage']

data = {'awakenings': awakenings}

for category in categories:
    counts = df[category].groupby(df['Awakenings']).mean()
    data[category] = counts.tolist()

source = ColumnDataSource(data = data)

plot = figure(x_range=awakenings, y_range=(0, 100),
           height=350, toolbar_location=None, tools="")

plot.vbar(x=dodge('awakenings', -0.25, range=plot.x_range), top='Light sleep percentage', source=source,
       width=0.2, color="#c9d9d3", legend_label="Light sleep percentage")

plot.vbar(x=dodge('awakenings',  0.0,  range=plot.x_range), top='Deep sleep percentage', source=source,
       width=0.2, color="#718dbf", legend_label="Deep sleep percentage")

plot.vbar(x=dodge('awakenings',  0.25, range=plot.x_range), top='REM sleep percentage', source=source,
       width=0.2, color="#e84d60", legend_label="REM sleep percentage")

plot.x_range.range_padding = 0.1
plot.xgrid.grid_line_color = None
plot.legend.location = "top_left"
plot.legend.orientation = "horizontal"

show(plot)
