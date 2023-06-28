import pandas as pd
from bokeh.plotting import ColumnDataSource

def create_column_data_source(csv_file):
    df = pd.read_csv(csv_file)
    source = ColumnDataSource(df)
    return source



