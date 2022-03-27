import dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'Simple Web Scraping Web-App'



# @server.route('/favicon.ico')
# def favicon():
#     return flask.send_from_directory(os.path.join(server.root_path, 'static'),
#                                      'favicon.ico')