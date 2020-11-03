import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Stylesheet:
stylesheet = ['https://codepend.io/chriddyp/pen/bWLwgP.css']

# App:
app = dash.Dash(__name__, external_stylesheets=stylesheet)

# App Layout:
app.layout = html.Div([
             html.H6("Change the value in the text box to see callbacks in action!"),
             html.Div(["Input: ",
                       dcc.Input(id='my-input',
                                 value='initial value',
                                 type='text')]),
             html.Br(),
             html.Div(id='my-output'),
])


# App Callback (decorator):
@app.callback(
     Output(component_id='my-output', component_property='children'),
     Input(component_id='my-input', component_property='value')
)
# Callback Function:
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


# Run:
if __name__ == '__main__':
    app.run_server(debug=True)
