import pandas as pd
import numpy as np
from dash import Dash, dcc, html
#correção de erros até conseguir utilizar o ambiente virtual
#agora definir a forma correta de acesso aos dados
df1 = pd.read_excel('c:/Users/UNB/Anexos_Balanço_TD - Março 2023.xlsx').query("type == 'conventional' and region == 'Albany'")
app = Dash(__name__)
print (df1)
app.layout = html.Div(
    children=[
        html.H1(children="Análise do Tesouro Direto"),
        html.P(
            children=(
                "Venda por prazo"
                "número de operações de venda por faixa de aplicação"
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Total"],
                        "y": data["Porcentagem"],
                       
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)