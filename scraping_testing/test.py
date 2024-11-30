import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def create_grid(rows, cols):
    return [[" " for _ in range(cols)]for _ in range(rows)]

def scrapped(url):
    
    r = requests.get(url)

    soup = bs(r.text, "html.parser")

    table = soup.find('table', class_='c8')
    titles = table.findAll('tr')[0]
    column_titles = []

    for title in titles:
        column_titles.append(title.text.strip())

    table_data = soup.findAll('tr')[1:]

    for row in table_data:
        row_data = row.findAll('td')
        
        indiv_row_data = [data.text.strip() for data in row_data] 

    df = pd.DataFrame(columns=column_titles)

    for row in table_data:
        row_data = row.findAll('td')
        
        indiv_row_data = [data.text.strip() for data in row_data]

        length = len(df)
        df.loc[length] = indiv_row_data

    row = 0
    
    grid = create_grid(100, 7)

    while row < length:
        
        x = df.iat[row, 0]
        y = df.iat[row, 2]
        c = df.iat[row, 1]
        
        grid[int(x)][int(y)] = c
        
        row += 1
        
    for sublist in grid:
        print(sublist)       
    
scrapped("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
