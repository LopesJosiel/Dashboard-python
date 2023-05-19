import pandas as pd
import numpy as np
from dash import Dash, dcc, html
import plotly.express as px 
app = Dash(__name__)
#correção de erros até conseguir utilizar o ambiente virtual
#agora definir a forma correta de acesso aos dados
#procurando configuração adequada para que o dash gere o gráfico

df = pd.DataFrame({
    "meses": ['Mar/22','Abr/22','Mai/22','Jun/22','Jul/22','Ago/22','Set/22','Out/22','Nov/22','Dez/22','Jan/23', 'Fev/23', 'Mar/23'],
    "Total": [ 17891025, 18392003, 18953067, 19492362, 20028345, 20665899, 21161249, 21600786, 22048922, 22483236, 23023837, 23355547, 23724147]
})

fig = px.bar(df, x="meses", y="Total")

app.layout = html.Div(children=[
    html.H1(children='Análise Tesouro Direto'),

    html.Div(children='''
        Tesouro: Total de investidores de março/2022 a março/2023.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)