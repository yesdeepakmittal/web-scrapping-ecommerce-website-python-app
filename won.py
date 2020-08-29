from app import app
from app import server
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output,State
from datetime import datetime
import dash_table
import pandas as pd
from decouple import config
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
	[Input('button','children')])
def kuchbhifunction(data):
	#output checking
	with open('string.txt') as file: 
		# for line in file.readlines()[-1:]: #reading last line of a file
		# 	print(line,end='')
		item = file.readlines()[-1:]
		item = ' '.join(item)
	product_fn(item)
	products = pd.read_csv('data.csv')
	fig = px.scatter(products,x='Product',y='Price(in Rs.)',size='Rating',color = 'Price(in Rs.)')
	# fig.update_layout(height)
	return html.Div([html.Div(children=[dcc.Graph(id='dist-chart', figure=fig)],
                            style={'display': 'inline-block', 'textAlign': 'center'})])


if __name__ == "__main__":
    app.run_server(debug=True)
