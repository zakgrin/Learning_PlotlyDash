import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Stylesheet:
stylesheet = ['https://codepend.io/chriddyp/pen/bWLwgP.css']

# App:
app = dash.Dash(__name__, external_stylesheets=stylesheet)

# DataFrame:
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Figure:
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# App Layout:
app.layout = html.Div(
             children=[html.H1(children='Hello Dash'),
                       html.Div(children='''
                                Dash: A web application framework for Python.
                                '''),
                       dcc.Graph(id='example-graph',
                                 figure=fig)
             ]
)

# Run:
if __name__ == '__main__':
    app.run_server(debug=True)
