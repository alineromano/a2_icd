# importando pandas 
import pandas as pd
# importando a estrutura de dados "ColumnDataSource" da biblioteca bokeh
from bokeh.plotting import ColumnDataSource

# criando a função que transforma os dados da base em ColumnDataSource
def create_column_data_source(csv_file):
    # usando pandas para ler a base de dados em formato csv
    df = pd.read_csv(csv_file)
    # tranformando cada coluna em lista e atribuindo isso a uma variavel
    source = ColumnDataSource(df)
    # retornando a variável com a "resposta" procurada
    return source

# Esse módulo basicamente transforma cada coluna da base de dados em uma lista, na qual os elementos são os dados contidos na coluna.
# Esse arquivo será usado nos outros para as realização das próximas etapas do trabalho.



