import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

# Stylesheet:
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# App:
app = dash.Dash(__name__, external_stylesheets=stylesheets)

# Layout:
app.layout = html.Div([
                html.Div([
                    'X = ',
                    dcc.Input(id='input', type='number', value=10)
                ],
                    style={'width': '49%', 'display': 'inline-block'}
                ),
                html.Div([
                    html.Td(['x', html.Sup('2'), ' = '], style={'display': 'inline-block'}),
                    html.Output(id='square')
                ]),
                html.Div([
                    html.Td(['x', html.Sup('3'), ' = '], style={'display': 'inline-block'}),
                    html.Output(id='cubic')
                ])
             ])


# Callback:
@app.callback([Output('square', 'children'),
               Output('cubic', 'children')],
              [Input('input', 'value')]
)
def update(x):
    if x is None:
        return None, None
    return x**2, x**3


# Run:
if __name__ == '__main__':
    app.run_server(debug=True)