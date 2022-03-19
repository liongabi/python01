#importing:

import random
import pandas as pd
import numpy as np
import datetime as dt
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup



""""
- PLANILHA 1: 4 COLUNAS - REGISTRO ID, NOME, DATA DE NASCIMENTO, IDADE
    -> RANDOM GENERATOR COM 5 DIGITOS (NÃO PODEM SE REPETIR)
    -> NOMES, PEGOS EM UMA PÁGINA WEB (WEB SCRAPPING)
    -> DATA DE NASCIMENTO, NO FORMATO AAAA-MM-DD, GERADOS DE FORMA ALEATÓRIA A PARTIR DE PARÂMETROS DE ENTRADA A DEFINIR
    -> CALCULADA NO MOMENTO DA GERAÇÃO DO BANCO: DATA ATUAL - DATA DE NASCIMENTO
    
- PLANILHA 2: 4 COLUNAS - REGISTRO ID, DATA DE SOLICITAÇÃO DE CRÉDITO, VALOR SOLICITADO, STATUS DA DÍVIDA
    -> REGISTRO ID IGUAL AO DE CIMA
    -> DATA ENTRE 2000 e 2021
    -> VALOR ENTRE $1K E $100K
    -> STATUS: "PAGO" OU "NÃO PAGO"
        
- COM ESSE BANCO DE 2 CSVs, IR PARA O MY SQL E FAZER A ANÁLISE DAS INFORMAÇÕES LÁ:
    -> EXTRAIR QUEM É A PESSOA COM MAIOR DÍVIDA PAGA E NÃO PAGA
    -> CLASSIFICAR OS CLIENTES EM "JOVENS", "ADULTOS", "IDOSOS" -> VER UMA CLASSIFICAÇÃO EXISTENTE E PARTIR DAÍ
    -> GERAR A TABELA DE ANÁLISE FINAL: ID, FAIXA ETÁRIA, VALOR DO EMPRÉSTIMO, STATUS

- NOVAMENTE AQUI, IMPORTAR A PLANILHA CSV COM DADOS FINAIS A SEREM ANALISADOS:
    -> VERIFICAR FILTRAGEM DE INCONSISTÊNCIAS (OUTLIERS)
    -> SELECIONAR MODELOS DE ML (CLASSIFICAÇÃO) E APLICAR
    -> DEFINIR QUAL PERFIL DE CREDOR QUE MENOS PAGA E QUAL MAIS PAGA SUAS DÍVIDAS.
    
- DIARIAMENTE, ALIMENTAR MEU GITHUB COM SEQUÊNCIA DO CÓDIGO;

- AO FINAL, ESCREVER UM POST PARA MEDIUM (EM INGLÊS) E UM POST PARA O LINKEDIN; 
     
"""

#database size: 5000 IDs

#creating lists:

def generator_ID():
    ID_generated=[]
    ID= list(range(10000, 1000000))
    for i in random.sample(ID, k=5000):
        ID_generated.append(i)
    return ID_generated


#FIRST NAME:
url_first_name= "https://www.ssa.gov/oact/babynames/decades/century.html"
headers_fisrt_name= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
req_first_name= Request(url_first_name, headers = headers_fisrt_name)
response_first_name= urlopen(req_first_name)
soup_first_name=BeautifulSoup(response_first_name, 'html.parser')
print(soup_first_name.prettify())

#LAST NAME:
url_last_name= "https://www.thoughtco.com/most-common-us-surnames-1422656"
headers_last_name= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
req_last_name= Request(url_last_name, headers = headers_last_name)
response_last_name= urlopen(req_last_name)
soup_last_name=BeautifulSoup(response_last_name, 'html.parser')
print(soup_last_name.prettify())



def names():



    #female_first_name=
    #male_first_name=





    pass

def birth_date():
    #AGE_YEAR=
    #AGE_MONTH=
    #AGE_DAY=
    #age= YYYY + - + MM + - + DD
    pass

def age():
    pass


#creating the table with the generated info:

ID= generator_ID()


#database = pd.DataFrame(np.random.randint(0,5000, size=(5000, 6)), columns=('ID', ))

#saving my table as csv file:

