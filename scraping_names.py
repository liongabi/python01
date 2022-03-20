from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

def last_name():
    url_last_name= "https://www.thoughtco.com/most-common-us-surnames-1422656"
    headers_last_name= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    req_last_name= Request(url_last_name, headers = headers_last_name)
    response_last_name= urlopen(req_last_name)
    soup_last_name=BeautifulSoup(response_last_name, 'html.parser')
    table_last_name=soup_last_name.find('table', class_='mntl-sc-block-table__table')

    last_name_list=[]
    for row in table_last_name.findAll("tr"):
        cells= row.findAll('td')
        if len(cells)==4:
            last_name_list.append(cells[1].find(text=True))

    return(last_name_list)

def female_first_name():
    url_first_name = "https://www.ssa.gov/oact/babynames/decades/century.html"
    headers_fisrt_name = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    req_first_name = Request(url_first_name, headers=headers_fisrt_name)
    response_first_name = urlopen(req_first_name)
    soup_first_name = BeautifulSoup(response_first_name, 'html.parser')
    table_first_name=soup_first_name.find('table', class_='t-stripe')

    female_first_name_list = []
    for row in table_first_name.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) == 5:
            female_first_name_list.append(cells[3].find(text=True))

    return (female_first_name_list)

def male_first_name():
    url_first_name = "https://www.ssa.gov/oact/babynames/decades/century.html"
    headers_fisrt_name = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    req_first_name = Request(url_first_name, headers=headers_fisrt_name)
    response_first_name = urlopen(req_first_name)
    soup_first_name = BeautifulSoup(response_first_name, 'html.parser')
    table_first_name=soup_first_name.find('table', class_='t-stripe')

    male_first_name_list = []
    for row in table_first_name.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) == 5:
            male_first_name_list.append((cells[1].find(text=True)))

    return (male_first_name_list)

male=male_first_name()
female=female_first_name()
last=last_name()

print(male)
print(female)
print(last)

