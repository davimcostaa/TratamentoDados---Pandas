# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:57:53 2022

@author: davi.costa
"""

import pandas as pd

## siafi = pd.read_excel() 
print(siafi)
siafi = siafi.drop(siafi.index[0:8]) #apaga as linhas do cabeçalho
print(siafi)

# # siafi.columns = ['Diretoria', 'CG', 'identificador', 'Fonte', 'PTRES', 'PI', 'PI Descrição', 'ÓRGÃO UG', 'UG', 'UG Descrição', 
# #                   'NDD', 'NDD Descrição','CRÉDITO DISPONÍVEL','DESPESAS PRE-EMPENHADAS A EMPENHAR','DESPESAS NÃO EMPENHADAS', 
# #                   'DESPESAS EMPENHADAS', 'DESPESAS EMPENHADAS A LIQUIDAR', 'DESPESAS LIQUIDADAS', 'TOTAL DESCENTRA-LIZADO'] #a tabela não veio com os nomes da coluna, coloquei manualmente

siafi = siafi.dropna(thresh=12)

# lista_cr = pd.read_excel()

lista_cr['UG']=lista_cr['UG'].astype(int) #troca o tipo da coluna para int
siafi['UG'] = siafi['UG'].astype(int) #troca o tipo da coluna para int
siafi = siafi.merge(lista_cr)   #une as tabelas pela coluna UG
 
siafi.drop(['ID', 'id_mapa'], axis=1, inplace=True) #apaga as colunas da tabela Lista_CR que vieram com o merge mas não são necessárias

siafi['UG Descrição'] = siafi['CR'] # coloca os nomes corretos das UG

siafi.drop(['CR'], axis=1, inplace=True) #apaga a coluna CR para não repetir os nomes.
print(siafi)

