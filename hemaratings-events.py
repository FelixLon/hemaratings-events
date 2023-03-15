import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = "https://hemaratings.com/events/"
  
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# request from hemaratings website
html_response = requests.get(url=url, headers = headers)
a = re.split('<h2>2022</h2>|<h2>2021</h2>|<h2>2020</h2>|<h2>2019</h2>|<h2>2018</h2>',html_response.text)

# get from local file - for testing
"""html_response = open("sample.html", "r")
index = html_response.read()
a = re.split('<h2>2022</h2>|<h2>2021</h2>|<h2>2020</h2>|<h2>2019</h2>|<h2>2018</h2>',index)"""

soup = BeautifulSoup(''.join(a[1:5]), 'html.parser')
events = soup.find_all("div", "panel-group")

#create list of objects (event details) using BeautifulSoup
elist = []
for e in events:
    year = e["id"].replace("accordion_", "")
    try:
        ev = {}
        ev["year"] = year
        ev["name"] = e.find("span", "event-title").get_text().strip()
        details = e.find_all("dd")
        ev["country"] = details[1].get_text()
        table = e.find("tbody")
        rows = table.find_all("tr")
        for r in rows:
            type = r.contents[1].get_text().lower().replace(" ", "").replace("'", "")
            ev[type+'_fights'] = int(r.contents[3].get_text())
            ev[type+'_fighters'] = int(r.contents[5].get_text())
        elist.append(ev)
    except:
       print("error") 

# create Pandas dataframe from event details
pd.options.display.max_columns = None
pd.set_option('max_colwidth', 1000)
df = pd.DataFrame(elist)
# sort by number of participants in event type (default mixed steel longsword)
df.sort_values(by=['mixedsteellongsword_fighters'], axis=0, ascending=[False], inplace=True) 
#df = df[~df['country'].isin(['United States'])] #uncomment to exclude US
df = df.style.format(precision=0)
df.to_excel("output.xlsx")  