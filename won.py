from app import app
from app import server
from dash import html, dcc
from dash.dependencies import Input, Output,State
import pandas as pd
import plotly.express as px

app.layout = html.Div([dcc.Input(id = 'input-box',
    placeholder='Enter a value...',
    type='text',
    value=''),
	html.Button('Submit', id='button'),
    html.Div(id='Output',children='Enter a value and press submit'),
    html.Div(id='table',children='Table is here')])

@app.callback(Output('Output','children'),
	[Input("button", "n_clicks")],
	[State('input-box', 'value')])
def update_output(n_clicks,input1):
	if input1 != None:
		string = open('string.txt','a+')
		string.write(str(input1))
		string.write('\n')
		string.close()
	
	return u'Input {input1} | \nNumber of clicks {click1}'.format(input1 = input1,click1 = n_clicks)

from data import product_fn
@app.callback(Output('table','children'),
	[Input('button','n_clicks')],
	[State('input-box', 'value')])
def kuchbhifunction(data,item_name):
	product_fn(item_name)
	products = pd.read_csv('data.csv')
	fig = px.scatter(products,x='Product',y='Price(in Rs.)',size='Rating',color = 'Price(in Rs.)')
	# fig.update_layout(height)
	fig.update_xaxes(showticklabels=False)
	return html.Div([html.Div(children=[dcc.Graph(id='dist-chart', figure=fig)],
                            style={'display': 'inline-block', 'textAlign': 'center'})])


if __name__ == "__main__":
    app.run_server(debug=True)
