import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Style:
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# DataFrame:
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# App:
app = dash.Dash(__name__, external_stylesheets=stylesheets)

# Layout:
app.layout = html.Div([
                dcc.Graph(id='graph-with-slider'),
                dcc.Slider(id='year-slider',
                           min=df['year'].min(),
                           max=df['year'].max(),
                           value=df['year'].min(),
                           marks={str(year): str(year) for year in df['year'].unique()},
                           step=None
                           )
])


# Callback:
@app.callback(Output('graph-with-slider', 'figure'),
              Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    fig = px.scatter(filtered_df,
                     x="gdpPercap",
                     y="lifeExp",
                     range_x=(df['gdpPercap'].min(), df['gdpPercap'].max()),
                     range_y=(df['lifeExp'].min(), df['lifeExp'].max()+10),
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=True,
                     size_max=55,
                     labels=dict(gdpPercap="GDP/Capita",
                                 lifeExp="Life Expectancy",
                                 pop="Population"))
    fig.update_layout(transition_duration=500)
    return fig


# Run:
if __name__ == '__main__':
    app.run_server(debug=True)