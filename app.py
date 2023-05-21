import pandas as pd
import numpy as np
from dash import Dash, dcc, html
import plotly.express as px 
app = Dash(__name__)
#correção de erros até conseguir utilizar o ambiente virtual
#agora definir a forma correta de acesso aos dados
#procurando configuração adequada para que o dash gere o gráfico
colors = {'background':'#FDFEFE','text': '#138D75', 'barras': '#2471A3'} 
#adicionando formatação de fundo e de texto
#dataframe para o gráfico de barras
df = pd.DataFrame({
    "meses": ['Mar/22','Abr/22','Mai/22','Jun/22','Jul/22','Ago/22','Set/22','Out/22','Nov/22','Dez/22','Jan/23', 'Fev/23', 'Mar/23'],
    "Total": [ 17891025, 18392003, 18953067, 19492362, 20028345, 20665899, 21161249, 21600786, 22048922, 22483236, 23023837, 23355547, 23724147]
}) 
fig = px.bar(df, x="meses", y="Total")
fig.update_layout(                  #adicionando configurações de visualização
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['barras'],
    font_color=colors['text'])
#dataframe para o gráfico de piza
df_faixa = pd.DataFrame ({
    "Faixa Etária":['Até 15 anos','De 16 a 25 anos','De 26 a 35 anos','De 36 a 45 anos','De 46 a 55 anos','De 56 a 65 anos','Maior de 66 anos'],
    "Participação por Faixa Etária": [0.003, 0.2326, 0.3451, 0.2361, 0.1027, 0.0518, 0.0288]})
#adicionando gráfico de setores para visualização de faixa etária
fig_pie = px.pie(df_faixa, values='Participação por Faixa Etária', names='Faixa Etária', title='Investidores por Faixa Etária') 
fig_pie.update_layout(                  #adicionando configurações de visualização
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['barras'],
    font_color=colors['text'])

app.layout = html.Div (children=[
    html.H1(children='Análise Tesouro Direto'), 
    style== {'textAlign': 'center', 'color':'text'},
    html.Div (children="Tesouro: Total de investidores de março/2022 a março/2023.",
    style= {'textAlign': 'center', 'color': 'text'})
    dcc.Graph( id='example-graph', figure=fig),
    dcc.Graph( id='example-graph', figure=fig_pie)
])
if __name__ == '__main__':
    app.run_server(debug=True)