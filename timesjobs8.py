from bs4 import BeautifulSoup
import requests 
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup=BeautifulSoup(html_text.text,'html.parser')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs :
    company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
    skills=job.find('span',class_='srp-skills').text.replace(' ','')
    published_date=job.find('span',class_='sim-posted').span.text
    print(f'''
    Company name : {company_name}
    skills : {skills}
    ''')
    print ('')