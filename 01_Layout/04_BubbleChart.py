import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

# Stylesheet:
stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# App:
app = dash.Dash(__name__, external_stylesheets=stylesheet)

# DataFrame:
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# Figure:
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

# Layout:
app.layout = html.Div([
                dcc.Graph(
                    id='life-exp-vs-gdp',
                    figure=fig
                )
])


# Run:
if __name__ == '__main__':
    app.run_server(debug=True)
