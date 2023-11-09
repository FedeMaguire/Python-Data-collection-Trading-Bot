import pandas as pd
import plotly.graph_objects as go

def data_http_viewer():
    df = pd.read_csv('historic_CHART_values.csv')
    df = df.sort_index(ascending=False)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',align='left'),
        cells=dict(values=[df['Time'], df['Open'], df['High'], df['Low'], 
                        df['Close'], df['stochrsi_k'], df['Buy'],df['Sell']],
                fill_color='lavender',align='left'))
    ])
    fig.show()

data_http_viewer()