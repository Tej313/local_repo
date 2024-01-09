import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})

# Check if there are at least 5 titles in the list
if len(titles) >= 5:
    print(titles[1].text)
else:
    print("Not enough titles found.")

