import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Generate some random data
np.random.seed(42)  # for reproducibility
data = np.random.randn(500)
df = pd.DataFrame({'data': data})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Histogram"),
    html.P("Adjust the number of bins using the slider below."),
    dcc.Slider(
        id='bin-slider',
        min=10,
        max=100,
        value=30,
        marks={str(i): str(i) for i in range(10, 101, 10)},
        step=1
    ),
    dcc.Graph(id='histogram'),
])


@app.callback(
    Output('histogram', 'figure'),
    Input('bin-slider', 'value')
)
def update_histogram(num_bins):
    fig = px.histogram(df, x='data', nbins=num_bins, title=f'Histogram with {num_bins} Bins')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)