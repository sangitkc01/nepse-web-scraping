from bs4 import BeautifulSoup
import requests

x=[]
n=int(input('enter pages = '))
for p in range(1,n+1):
    url=BeautifulSoup(f"http://www.nepalstock.com/main/todays_price/index/{p}/","html.parser")
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"lxml")

    share_box=soup.find("table",class_="table table-condensed table-hover")
    rows=share_box.find_all("tr")

    for index,row in enumerate(rows):
        if  index==0:
            continue
        elif index==1:
            heads=row.text
            heads=heads.split("\n")
            x.append(heads[1:-1])
        elif index==22:
            break
        else:
            data=row.text
            data=data.split("\n")
            x.append(data[1:-3])

import csv
with open("new.csv","w",newline="") as csvfile:
    wr=csv.writer(csvfile)
    wr.writerows(x)

import pandas as pd
df=pd.read_csv("new.csv",encoding = "ISO-8859-1",index_col="S.N.")
dff=df.drop("S.N.")
final_data=dff.to_csv("new2.csv")