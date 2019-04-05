import bs4
import requests
import pandas as pd

#replace the ticker below with the relevant ticker for your stock
url = "https://hk.finance.yahoo.com/quote/1257.HK/history?p=1257.HK"

def table_to_df(table):
    return pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])


page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
table = soup.find(name='table', attrs={'data-test':'historical-prices'})

res = pd.DataFrame()
res = res.append(table_to_df(table))

res.to_csv("table.csv", index=None, sep=';')
