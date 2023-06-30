from bokeh.layouts import gridplot
from bokeh.io import output_file, show

from plot1 import create_plot1
from plot5 import create_plot5
from plot6 import create_plot6

# importando as funções para criar os plots
plot1 = create_plot1()
plot5 = create_plot5()
plot6 = create_plot6()

# montando o grid
grid = gridplot([[plot6, plot1], [plot5, None]], sizing_mode="scale_width")

# definindo o html
output_file("grid_plot.html")

show(grid)
