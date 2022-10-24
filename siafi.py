# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:57:53 2022

@author: davi.costa
"""

import pandas as pd

siafi = pd.read_excel("Z:/CGETNO/CGETNO/Estágio/Davi/siafi.xlsx", sheet_name = 'CGETNO', header=9) 
print(siafi)
siafi = siafi.drop(siafi.index[0:8]) #apaga as linhas do cabeçalho
print(siafi)

# # siafi.columns = ['Diretoria', 'CG', 'identificador', 'Fonte', 'PTRES', 'PI', 'PI Descrição', 'ÓRGÃO UG', 'UG', 'UG Descrição', 
# #                   'NDD', 'NDD Descrição','CRÉDITO DISPONÍVEL','DESPESAS PRE-EMPENHADAS A EMPENHAR','DESPESAS NÃO EMPENHADAS', 
# #                   'DESPESAS EMPENHADAS', 'DESPESAS EMPENHADAS A LIQUIDAR', 'DESPESAS LIQUIDADAS', 'TOTAL DESCENTRA-LIZADO'] #a tabela não veio com os nomes da coluna, coloquei manualmente

siafi = siafi.dropna(thresh=12)

lista_cr = pd.read_excel("Z:/CGETNO/CGETNO/Estágio/Davi/listas_formulário 1.xlsx", sheet_name = 'Lista_CR')

lista_cr['UG']=lista_cr['UG'].astype(int) #troca o tipo da coluna para int
siafi['UG'] = siafi['UG'].astype(int) #troca o tipo da coluna para int
siafi = siafi.merge(lista_cr)   #une as tabelas pela coluna UG
 
siafi.drop(['ID', 'id_mapa'], axis=1, inplace=True) #apaga as colunas da tabela Lista_CR que vieram com o merge mas não são necessárias

siafi['UG Descrição'] = siafi['CR'] # coloca os nomes corretos das UG

siafi.drop(['CR'], axis=1, inplace=True) #apaga a coluna CR para não repetir os nomes.
print(siafi)


import psycopg2
conect2 = psycopg2.connect(host='localhost', database='siafi',
user='postgres', password='1234')

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:1234@localhost:5432/siafi')


siafi.to_sql('siafi', engine, schema='teste_siafi')

print(siafi)

file_name = 'siafi_corrigido3.xlsx' # determinando nome do arquivo
  
siafi.to_excel(file_name) #nome do arquivo
# print('DataFrame convertido em Excel com sucesso.')

import os
excel = pd.ExcelWriter('Z:/CGETNO/CGETNO/Estágio/Davi/siaficorrigido3.xlsx', engine='xlsxwriter')
siafi.to_excel(excel)
excel.save()