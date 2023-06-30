from bokeh.layouts import gridplot
from bokeh.io import output_file, show

from plot1 import create_plot1
from plot2 import create_plot2, create_plot3, create_plot4
from plot5 import create_plot5
from plot6 import create_plot6
from plot_1_ana_julia import create_plot7
from plot_2_ana_julia import create_plot8
from plot_3_Ana import create_plot9


# importando as funções para criar os plots
plot1 = create_plot1()
plot2 = create_plot2()
plot3 = create_plot3()
plot4 = create_plot4()
plot5 = create_plot5()
plot6 = create_plot6()
plot7 = create_plot7()
plot8 = create_plot8()
plot9 = create_plot9()


# montando o grid
grid = gridplot([[plot6, plot1], [plot5, plot7], [plot8, plot2], [plot3, plot4], [plot9, None]], sizing_mode="scale_width")

# definindo o html
output_file("index.html")

show(grid)


