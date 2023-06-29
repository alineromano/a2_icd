from bokeh.io import show
from bokeh.models import BasicTicker, ColorBar, FactorRange, LinearColorMapper
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from base_limpa import df
from ICdD_modulo_base_para_cds import create_column_data_source

# definindo o columdatasource
csv_file  = 'Sleep_Efficiency_Limpa.csv'
source = create_column_data_source(csv_file)

colors = ["#EDE5A8", "#d5caa1", "#b3aa98", "#807a8b", "#4c497e", "#191970"]

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

bedtime = ['21:00:00', '21:30:00', '22:00:00', '22:30:00', '23:00:00', '00:00:00', '00:30:00', '01:00:00', '01:30:00', '02:00:00', '02:30:00']

wakeuptime = df['Wakeup time'].unique().astype(str).tolist()
wakeuptime.sort()

x_factors = bedtime
y_factors = wakeuptime

plot = figure(title="Sleep Duration on the Clock",
              x_range=FactorRange(factors=x_factors), y_range=FactorRange(factors=y_factors),
              x_axis_location="above", width=900, height=400,
              tools=TOOLS, toolbar_location='below')

plot.rect(x="Bedtime", y="Wakeup time", width=1, height=1, source=source,
              fill_color=linear_cmap("Sleep duration", colors, low=df["Sleep duration"].min(), high=df["Sleep duration"].max()),
              line_color=None)

color_mapper = LinearColorMapper(palette=colors, low=df["Sleep duration"].min(), high=df["Sleep duration"].max())
color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker())

plot.add_layout(color_bar, 'right')

show(plot)