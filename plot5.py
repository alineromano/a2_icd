from bokeh.io import output_file, show
from bokeh.models import Range1d
from bokeh.models.annotations import BoxAnnotation
from bokeh.plotting import figure
from ICdD_modulo_base_para_cds import create_column_data_source

csv_file  = 'Sleep_Efficiency.csv'
source = create_column_data_source(csv_file)

plot = figure()

palette = ['red', 'green']

plot.circle(x="Deep sleep percentage", y="Light sleep percentage", size = "Sleep efficiency", source = source)

plot.xaxis.axis_label = "Deep sleep percentage"
plot.yaxis.axis_label = "Light sleep percentage"

plot.x_range = Range1d(start = 0, end = 80)
plot.y_range = Range1d(start = 0, end = 70)

box_annotation1 = BoxAnnotation(left = 15, right = 40, top = 65, bottom = 35, fill_color = "red", fill_alpha = 0.42)
plot.add_layout(box_annotation1)

box_annotation2 = BoxAnnotation(left = 47, right = 78, top = 33, bottom = 5, fill_color = "green", fill_alpha = 0.42)
plot.add_layout(box_annotation2)

show(plot)