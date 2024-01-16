from bs4 import BeautifulSoup
import requests 
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup=BeautifulSoup(html_text.text,'html.parser')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
print (jobs)