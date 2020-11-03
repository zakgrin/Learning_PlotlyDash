import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Stylesheet:
stylesheet = ['https://codepend.io/chriddyp/pen/bWLwgP.css']

# App:
app = dash.Dash(__name__, external_stylesheets=stylesheet)

# ** Colors:
colors = {'background': '#111111',
          'text': '#7FDBFF'
          }

# DataFrame:
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Figure:
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# ** Figure Update:
fig.update_layout(plot_bgcolor=colors['background'],
                  paper_bgcolor=colors['background'],
                  font_color=colors['text']
                  )


# App Layout:
app.layout = html.Div(
             style={'backgroundColor': colors['background']},  # ** update
             children=[html.H1(children='Hello Dash',
                               style={'textAlign': 'center',  # ** update
                                      'color': colors['text']  # ** update
                                      }
                               ),
                       html.Div(children='''Dash: A web application framework for Python.''',
                                style={'textAlign': 'center',  # ** update
                                       'color': colors['text']  # ** update
                                       }
                                ),
                       dcc.Graph(id='example-graph',
                                 figure=fig)
                       ]
)

# Run:
if __name__ == '__main__':
    app.run_server(debug=True)
