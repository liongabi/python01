from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import random

def name():
    url = "https://www.ssa.gov/oact/babynames/decades/century.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    req = Request(url, headers=headers)
    response = urlopen(req)
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find('table', class_='t-stripe')

    name_list = []

    for row in table.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) == 5:
            name_list.append(cells[3].find(text=True))

    name = random.choice(name_list)
    return name

name=name()
print("The name is: {}!".format(name))


