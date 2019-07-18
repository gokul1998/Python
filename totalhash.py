import requests 
from bs4 import BeautifulSoup 
import re
from pandas import DataFrame
'''
res will contain the resuls that will be used to convert it into a CSV file
res is List of Lists
'''
res = []
inc = 20
'''
generating URL for each pages which shows 20 entries per page
'''
for i in range(60):
    if i == 0:
        url = "https://totalhash.cymru.com/search/?av:*hash*%20or%20registry:*hash"
    else:
        url = "https://totalhash.cymru.com/search/?av:*hash*%20or%20registry:*hash/" + str(inc)
        inc += 20
    print(url)
    r = requests.get(url) 
    #print(r.headers['Set-Cookie'])
    src = r.content
    soup = BeautifulSoup(src,'html5lib')
    ''' 
    create a BeautifulSoup object for the generated url 
    '''
    table = soup.find('tbody')
    children = table.findChildren("tr",recursive=False)
    ''' 
    grab all the rows inside the table 
    each row contains four td cells
    '''
    #print(table)
    for child in children:
        curr = []
        '''
        first td cell will contain a Anchor tag inside a Span tag
        this Anchor tag will contain the hash value
        '''
        a = child.findChild("a")
        if a:
            curr.append(a.text)
        data = child.findChildren("td",recursive=True)
        '''
        traverse all the td cells in a row
        look for attribute width which is equal to 15%
        this will contain the timestamp of the hash
        '''
        #print(a)
        for tdata in data:
            if tdata.has_attr("width"):
                if tdata.attrs["width"] == "15%":
                    curr.append(tdata.text)
        '''
        curr is list containing data of the current row
        append it to the resultant list
        '''
        res.append(curr)

#print(res)
'''
convert the resultant list into a DataFrame
then save it in CSV format
'''
df = DataFrame.from_records(res)
df.to_csv("/Users/gokulakrishnan.parir/Desktop/Scrap_totalhash.csv") 