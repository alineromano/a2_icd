from bokeh.io import show
from bokeh.models import BasicTicker, ColorBar, FactorRange, LinearColorMapper
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from base_limpa import df
from ICdD_modulo_base_para_cds import create_column_data_source

# gráfico heatmat dos horários de deitar e acordar

def create_plot6():

    # definindo o columdatasource
    csv_file  = 'Sleep_Efficiency_Limpa.csv'
    source = create_column_data_source(csv_file)

    # paleta de cores degradê
    colors = ["#EDE5A8", "#d5caa1", "#b3aa98", "#807a8b", "#4c497e", "#191970"]

    # define os possíveis horários de bedtime (não foram extraídos da coluna pois não eram ordenáveis com sort)
    bedtime = ['21:00:00', '21:30:00', '22:00:00', '22:30:00', '23:00:00', '00:00:00', '00:30:00', '01:00:00', '01:30:00', '02:00:00', '02:30:00']

    # definindo os horários de wakeup
    wakeuptime = df['Wakeup time'].unique().astype(str).tolist() # lista os valores únicos de Awakenings
    wakeuptime.sort() # ordena

    # define essas variáveis como os fatores
    x_factors = bedtime
    y_factors = wakeuptime

    # define intervalo de x, y, as ferramentas de interação e coloca o eixo x em cima
    plot = figure(x_range = FactorRange(factors = x_factors), y_range = FactorRange(factors = y_factors), x_axis_location = "above")

    # plota os retângulos do heatmap e define a cor baseada em Sleep duration
    r = plot.rect(x="Bedtime", y="Wakeup time", width=1, height=1, source=source,
                fill_color=linear_cmap("Sleep duration", colors, low=df["Sleep duration"].min(), high=df["Sleep duration"].max()),
                line_color=None)

    # mapeamento das cores na escala com a paleta
    color_mapper = LinearColorMapper(palette=colors, low=df["Sleep duration"].min(), high=df["Sleep duration"].max())

    # adiciona a escala de cor
    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker())
    plot.add_layout(color_bar, 'right')

    # título
    plot.title = "Sleep Duration on the Clock"

    # estética
    plot.toolbar_location='below'
    plot.width = 900
    plot.height=400

    #show(plot)
    return plot