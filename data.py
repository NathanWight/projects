import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv

url_scrape = "https://en.wikipedia.org/wiki/Kawhi_Leonard"

request_page = urlopen(url_scrape)
page_html = request_page.read()
request_page.close()

html_soup = bs(page_html, 'html.parser')

#print(page_html)

stats = html_soup.find("table", class_= "wikitable sortable")
columns = stats.find("tr").find_all(["abbr","th"])
column_names = [str(c.string).strip() for c in columns]






table_rows = stats.find("tbody").find_all(["td","a"])
#print(table_rows)
row_names = [str(r.string).strip() for r in table_rows]


for row in row_names[:]:
    if row == 'None':
        row_names.remove(row)
    row.strip('')
for column in column_names[:]:
    if column == 'None':
        column_names.remove(column)
    column.strip('')



index = 0
i = 0
list1 = []
for row in row_names[index:]:
    det = 13
    if row == "Career":
        det = 12
    
    list1.append(row)
    
    i += 1
    if i == det:
        index += 12
        print(list1)
        i = 0
        
        list1.clear()
        print(list1)
print(row_names)