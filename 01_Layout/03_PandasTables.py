import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# DataFrame
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# Generate Table Function
def generate_table(dataframe, max_rows=10):
    table = html.Table([
                html.Thead(
                    html.Tr([html.Th(col) for col in dataframe.columns])
                ),
                html.Tbody([
                    html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))
                ])
            ])
    return table


# Stylesheet
stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# App
app = dash.Dash(__name__, external_stylesheets=stylesheet)

# Layout
app.layout = html.Div(
                children=[
                    html.H4('US Agriculture Exports (2011)'),
                    generate_table(df)
                ]
)

# Run
if __name__ == '__main__':
    app.run_server(debug=True)
