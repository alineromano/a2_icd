from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d
from ICdD_modulo_base_para_cds import create_column_data_source

csv_file = "Sleep_Efficiency_Limpa.csv"
source = create_column_data_source(csv_file)

# Resolvi analisar a relação entre a frequência de exercício físico e a duração do sono.
# Plotando o gráfico com os dados da tabela sem fazer nenhuma "alteração", ou seja, sem observar seus valores únicos, fazer porcentagem ou
# algo assim, já percebi que o gráfico fica bem estranho e disperso. Então, vou tentar explorar melhor esses dados para fazer um 
# gráfico mais legível e com bom aproveito das informações. 

# Criar o gráfico de dispersão
p = figure(title="Relação entre duração do sono e frequência de exercício físico",
           x_axis_label="Sleep duration",
           y_axis_label="Exercise frequency",
           width=800, height=600)

# Definir os intervalos dos eixos
x_range = Range1d(start=0, end=80)
y_range = Range1d(start=0, end=70)
p.x_range = x_range
p.y_range = y_range

# Adicionar a imagem como plano de fundo
background_image_url = '..\imagem_sono_exercicio_fisico.png'
background_opacity = 0.15
p.image_url(url=[background_image_url], x=0, y=0, w=80, h=70, anchor="bottom_left", alpha=background_opacity)

# Exibir o gráfico
show(p)


