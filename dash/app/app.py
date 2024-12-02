import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Generate some random data
np.random.seed(42)  # for reproducibility
data = np.random.randn(500)
df = pd.DataFrame({'data': data})

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1("Interactive Dashboard v2"),
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
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])


@app.callback(
    Output('histogram', 'figure'),
    Input('bin-slider', 'value')
)
def update_histogram(num_bins):
    fig = px.histogram(df, x='data', nbins=num_bins, title=f'Histogram with {num_bins} Bins')
    return fig

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)