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

#quanto maior o consumo de cafeína, menor a ocorrência de um sono profundo
y_range_start = 0
y_range_end = 110

p = figure(plot_width=600, plot_height=400, title="Relação entre consumo de cafeína e sono profundo", background_fill_color="#38375c",
           x_axis_label="Sono profundo", y_axis_label="Consumo de cafeina", y_range=(y_range_start, y_range_end))

p.star(x=df['Deep sleep percentage'], y=df['Caffeine consumption'], size=14, fill_color='#f2e6c9', line_color='#f2e6c9', alpha=0.5)

p.grid.grid_line_width = 1

output_notebook()
show(p)
