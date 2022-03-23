#importing:

import random
import names
from datetime import date, timedelta
from random import choices
import pandas as pd
from pathlib import Path

print("Initialization...")

def generator_ID():
    ID_generated=[]
    ID= list(range(10000, 1000000))
    for i in random.sample(ID, k=5000):
        ID_generated.append(i)
    return ID_generated

def birth_date_list():
    d0 = date(1920, 1, 1)
    df = date(2003, 12, 31)
    k = 5000
    dates = []

    while d0 != df:
        d0 += timedelta(days=1)
        d02 = d0.isoformat()
        dates.append(d02)
    list_dates = choices(dates, k=k)

    return list_dates

def female_full_name():
    female_full_name=[]
    for i in range(2500):
        rand_female_name= names.get_full_name(gender='female')
        female_full_name.append(rand_female_name)
    return(female_full_name)

def male_full_name():
    male_full_name=[]
    for i in range(2500):
        rand_male_name= names.get_full_name(gender='male')
        male_full_name.append(rand_male_name)
    return(male_full_name)

def names_list():
    female_names = female_full_name()
    male_names = male_full_name()
    names = female_names + male_names

    return names

def sex_list():
    female_sex_list=[]
    contador_female=0

    while contador_female < 2500:
        female_sex_list.append('F')
        contador_female += 1

    male_sex_list=[]
    contador_male=0

    while contador_male < 2500:
        male_sex_list.append('M')
        contador_male += 1

    sex_list= female_sex_list + male_sex_list
    return(sex_list)

def date_credit_request():
    d0 = date(2000, 1, 1)
    df = date(2021, 12, 31)
    k = 5000
    dates = []

    while d0 != df:
        d0 += timedelta(days=1)
        d02 = d0.isoformat()
        dates.append(d02)
    list_dates = choices(dates, k=k)

    return list_dates

def credit_value():
    credit_value_list=[i for i in random.sample(list(range(1000, 100000)), k=5000)]
    return credit_value_list

def status_debt():
    s=['PAYED', 'NOT PAYED']
    status_list= [[i for i in random.sample(s, k=1)] for i in range(0,5000)]
    return status_list

print("Functions OK!")

#variables:

ID = generator_ID()
name = names_list()
sex=sex_list()
birth_date=birth_date_list()
credit_request= date_credit_request()
credit= credit_value()
status= status_debt()

print("Variables OK!")

#creating the first table with the generated information:

table_01 = {'ID':ID, 'Name': name, 'Sex': sex, 'Birth': birth_date}
tb01= pd.DataFrame(data=table_01)

table_02 = {'ID':ID, 'Date credit request': credit_request, 'Value': credit, 'Status': status}
tb02= pd.DataFrame(data=table_02)

filepath= Path('G:/Meu Drive/table_01.csv') #table 01
filepath.parent.mkdir(parents=True, exist_ok=True)
tb01.to_csv(filepath, index=False)
print("Table 01 OK!")

filepath= Path('G:/Meu Drive/table_02.csv') #table 01
filepath.parent.mkdir(parents=True, exist_ok=True)
tb02.to_csv(filepath, index=False)
print("Table 02 OK!")