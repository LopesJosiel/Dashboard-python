import pandas as pd
import numpy as np
from dash import Dash, dcc, html
import plotly.express as px 

# Para usar Dash, você precisa criar uma instância do Dash. 
# 'name' é geralmente substituído por '__name__' para indicar o script atual.
app = Dash(__name__)

colors = {
    'background':'#FDFEFE',
    'text': '#138D75', 
    'barras': '#2471A3'
}
#dataframe para o gráfico de barras.
df = pd.DataFrame({ 
    "meses": [
        'Mar/22','Abr/22','Mai/22','Jun/22','Jul/22',
        'Ago/22','Set/22','Out/22','Nov/22','Dez/22',
        'Jan/23', 'Fev/23', 'Mar/23'
    ],
    "Total": [
        17891025, 18392003, 18953067, 19492362, 20028345, 
        20665899, 21161249, 21600786, 22048922, 22483236, 
        23023837, 23355547, 23724147
    ]
})
# Crie o gráfico de barras usando plotly
fig = px.bar(df, x="meses", y="Total")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['barras'],
    font_color=colors['text']
)

# Criação de um DataFrame separado para a distribuição por faixa etária
df_age = pd.DataFrame({
    "Faixa Etária": [
        'Até 15 anos', 'De 16 a 25 anos', 'De 26 a 35 anos', 
        'De 36 a 45 anos', 'De 46 a 55 anos', 'De 56 a 65 anos',
        'Maior de 66 anos'
    ],
    "Participação por Faixa Etária": [0.003, 0.2326, 0.3451, 0.2361, 0.1027, 0.0518, 0.0288]
})
# Criação do gráfico de pizza
fig_pie = px.pie(df_age, values='Participação por Faixa Etária', names='Faixa Etária', title='Investidores por Faixa Etária')

fig_pie.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['barras'],
    font_color=colors['text']
)
#layout do dashboard
app.layout = html.Div(children=[
    html.H1('Análise Tesouro Direto', style = {'textAlign': 'center', 'color':colors['text']}),
    html.Div("Tesouro: Total de investidores de março/2022 a março/2023.", style = {'textAlign':'center','color':colors['text']}),
    #inserindo parte responsiva para o dash
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    dcc.Graph(id='example-graph', figure=fig),
    dcc.Graph(id='example-pie', figure=fig_pie),
    html.Br(),
    html.Div(id='my-output'),
])
#incluir função para call back
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'
#consertar o output
if __name__ == '__main__':
    app.run_server(debug=True)