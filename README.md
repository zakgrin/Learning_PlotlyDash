# Learning Plotly Dash

In this repo, I share my learning for Plotly Dash which can be used to build ML/AI applications. Important notes about my
learning will be documented here as questions. Dash [tutorial](https://dash.plotly.com/installation) is the main reference.

# Questions

## What are the main parts of Dash apps?
-  `layout`
- Callback Functions

## What are the main classes in Dash?
- `dash_core_components`
- `dash_html_components`

(note: you can also build your own with JS and React.js). 

## How Dash apps are usually excuted?
Python code should be saved in files and excuted using `python app.py`. 


# Exercises

## Layout
### Hello Dash
![image](01_Layout\01_HelloDash.png)
- File: [`01_HelloDash.py`](01_Layout/01_HelloDash.py)
- Important Notes: 
    - `children` property is always the first attribute and can be omitted. 
        - `html.H1(children='Hello Dash')` == `html.H1('Hello Dash')`
        - it can contain: a string, a number, a signle component, or a list of components. 
        
### Customized Hello Dash
- File: [`02_CustomizedHelloDash.py`](01_Layout/02_CustomizedHelloDash.py)
- Important Notes: 
    - The style is added as a dictionary to `dash_html_components` 
      (while in html, `style` is a semicolon-separated string). 
    - Keys in `style` are camelCased (e.g. `textAlign` instead of `text_align`). 
    - Html `class` attribute is `className` in Dash.
    
### Pandas Table
- File: [`03_PandasTable`](01_Layout/03_PandasTables.py) 
    
### Bubble Chart
- File: [`04_BubbleChart.py`](01_Layout/03_PandasTables.py)

## Callback
### Basic
- File: [`01_Callback.py`](02_Callback/01_Callback.py) 
- Notes: 