# início construção dashboard em python
## procurar bases de dados sobre investimentos
#noções de HTML para fazer o layout em das
#dash HTML components (ver alguns componentes para utilização)
#dash core components
## Base de dados localizada (informações do tesouro direto)
### instalação do gerenciador de pacotes do windows CHOCOLATEY
#criação de ambiente virtual para instalação de versão específica do DASH e do PANDAS
#<!- comentário da parte do HTML do código-->
#<p> Análise do <strong>Tesouro Direto</srong></p>
import pandas as pd
from dash import Dash, dcc, html

df = pd.read_excel ('Anexos_Balanço_TD - Março 2023.xlsx')

app = Dash(__name__)
print (df)
