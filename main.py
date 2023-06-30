from bokeh.layouts import gridplot
from bokeh.io import output_file, show
from bokeh.plotting import curdoc

from plot1 import create_plot1
from plot5 import create_plot5
from plot6 import create_plot6
from rascunhos_plot_1_ana_julia import create_plot7
from plot_2_ana_julia import create_plot8


# importando as funções para criar os plots
plot1 = create_plot1()
plot5 = create_plot5()
plot6 = create_plot6()
plot7 = create_plot7()
plot8 = create_plot8()

# montando o grid
grid = gridplot([[plot6, plot1], [plot5, plot7], [plot8, None]], sizing_mode="scale_width")

# definindo o html
output_file("index.html")

show(grid)


