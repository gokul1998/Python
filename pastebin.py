import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
import re
from pandas import DataFrame

# source
URL = "https://pastebin.com/u/jroosen/2"
r = requests.get(URL) 
#print(r.headers['Set-Cookie'])
src = r.content
soup = BeautifulSoup(src,'html5lib')


#table = soup.find('tr',{'data-index':'0'})
#print(table.find('td').text)

table = soup.find('tbody')
#ßprint(table)
a_tag = []
children = table.findChildren('tr',recursive=False)
for child in children:
    data = child.findChild("td",recursive=False)
    #if data.findChild("a",recursive=False) != None:
    if data!=None:
        a_tag.append(data.findChild("a",recursive=False).get("href"))

res = []
li_tags = []
for link in a_tag:
        URL = "https://pastebin.com" + link
        r = requests.get(URL) 
        print(URL)
        #print(r.headers['Set-Cookie'])
        src = r.content
        soup = BeautifulSoup(src,'html5lib')
        ol = soup.find('ol',{'class':'text'})
        #print(ol)
        if ol:
                li_tags = ol.findChildren('li',recursive=False)
        for li in li_tags:
                #print(li.text)
                div_tag = li.findChild('div',recursive=False)
                text = div_tag.text
                if text.find("Creation") != -1:
                        #print(text)
                        res.append(text)
                #print(text)
                x = re.search("[A-Fa-f0-9]{64}",text)
                if x:
                        res.append(text)

final = []
time = ""
for item in res:
        curr = []
        if item.find("Creation") != -1:
                time = item[15:]
                continue
        curr.append(time)
        curr.append(item)
        final.append(curr)

#print(final)
df = DataFrame.from_records(final)
df.to_csv("/Users/gokulakrishnan.parir/Desktop/Scrap_bin.csv") 

