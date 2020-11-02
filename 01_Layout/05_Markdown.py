import dash
import dash_html_components as html
import dash_core_components as dcc

# Stylesheet
stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# App
app = dash.Dash(__name__, external_stylesheets=stylesheet)

# Markdown Text
markdown_text = '''
### Dash and Markdown
Dash apps can be written in Markdown. 
Dash uses the [commonMark](http://commonmark.org/)
specification of Markdown.
Check out [60 Second Markdown Tutorial](http://commonmark.org/help/). 
'''

# Layout
app.layout = html.Div([
                dcc.Markdown(children=markdown_text)
])

# Run
if __name__ == '__main__':
    app.run_server(debug=True)
