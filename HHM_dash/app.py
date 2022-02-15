# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from main import neuron
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output

app = Dash(__name__)

def run_server(self,
               port=5051,
               debug=True,
               threaded=True,
               **flask_run_options):
    self.server.run(port=port, debug=debug, **flask_run_options)

app.layout = html.Div(className="row", children=[
    html.Div(children=[
        html.H1(children='Hodgkin–Huxley model of a neuron', style={'textAlign': 'center'}),

        html.Div(children='''
            Simulation of a squid giant axon using Hodgkin–Huxley model.
        ''', style={'textAlign': 'center'}),
        html.Div(children='''
            Adjust the slider on the right in order to change the current applied to the patch.
        ''', style={'textAlign': 'center'})
        ]),
    html.Div(className="row", children=[  
        html.Div(className='six columns',children=[
            dcc.Graph(
                id='graph_with_slider',
                style={'width': '150vh', 'height': '69vh'},
            )], style=dict(width='80%')),

        html.Div(className='six columns',children = [
            dcc.Slider(
                id="slider-circular", min=0, max=3,
                marks={i: str(i) for i in range(4)},
                value=3,
                vertical=True,
                verticalHeight= 550)
            ], style=dict(width='20%'))], style=dict(display='flex'))
    ], 
)

@app.callback(
    Output("graph_with_slider", "figure"),
    Input("slider-circular", "value"),
)

def update_figure(current):
    n = neuron(inj_curr= current)
    v, i, t = n.run_hh_sim()

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Time": t,
        "Voltage": v,
        "Current": i
    })
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=t, y=v, mode='lines', name="Vm (mV)"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=t, y=np.array(i)/10, mode='lines', name="I (nA)"),
        secondary_y=True,
    )


    # Set x-axis title
    fig.update_xaxes(title_text="<b>Time</b> (msec)")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Voltage</b> (mV)", secondary_y=False)
    fig.update_yaxes(title_text="<b>Current</b> (nA)", secondary_y=True)

    fig.update_layout(legend_x=0, legend_y=1)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port = 8051)