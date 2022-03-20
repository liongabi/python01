#importing:
import datetime
import random
import pandas as pd
import numpy as np
import datetime as dt
import names
from random import randrange
from datetime import datetime
from datetime import date, timedelta
from random import choices



def generator_ID():
    ID_generated=[]
    ID= list(range(10000, 1000000))
    for i in random.sample(ID, k=5000):
        ID_generated.append(i)
    return ID_generated

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

def birth_date():
    d0 = date(1920, 1, 1)
    df = date(2003, 12, 31)
    k = 5000
    dates = []

    while d0 != df:
        d0 += timedelta(days=1)
        d02 = d0.strftime('%Y-%m-%d')
        dates.append(d02)
    list_dates = choices(dates, k=k)

    return list_dates

def age():


    pass

