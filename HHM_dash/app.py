# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from main import neuron

app = Dash(__name__)

def run_server(self,
               port=5051,
               debug=True,
               threaded=True,
               **flask_run_options):
    self.server.run(port=port, debug=debug, **flask_run_options)

n = neuron()
v, i, t = n.run_hh_sim()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Time": t,
    "Voltage": v,
    "Current": i
})

fig = px.line(df, x="Time", y="Voltage")

app.layout = html.Div(children=[
    html.H1(children='Hodgkin–Huxley model of a neuron'),

    html.Div(children='''
        Simulation of a squid giant axon using Hodgkin–Huxley model.
    '''),

    dcc.Graph(
        id='plot',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port = 8051)