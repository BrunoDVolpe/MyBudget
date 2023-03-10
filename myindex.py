from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, dashboards, extratos

from globals import *


# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dcc.Store(id='store-receitas', data=df_receitas.to_dict()),
    dcc.Store(id='store-despesas', data=df_despesas.to_dict()),
    dcc.Store(id='stored-cat-receitas', data=df_cat_receita.to_dict()),
    dcc.Store(id='stored-cat-despesas', data=df_cat_despesa.to_dict()),

    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])

], fluid=True,)
#Esse layout é a disponibilização do conteúdo na tela. Criei uma linha com duas colunas. Usa os fundamentos
#do bootstrap. Ou seja, a primeira coluna usa 2/12 avos da tela e a outra 10/12 avos da tela.
#fluid = True faz com que a disposição dos itens se espalhem de acordo com o tamanho da tela.

#callback (Outputs, que são os resultados do callback, ou seja, alterar as children do page content)
#Inputs, dentro de uma lista, será o id url e o pathname é o que queremos extrair pra função abaixo.
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
    #Debug = true significa que cada atualização aqui será refletida imediatamente no projeto.
    # False eu precisaria reiniciar o navegador e projeto.