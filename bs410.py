import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org/page/'

for page in range(1, 10):
    req = requests.get(f'{URL}{page}/')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class': 'head'})

    for i in range(4, min(19, len(titles))):  # Adjust the range to stay within the length of titles
        if page > 1:
            print(f'{(i - 3) + page * 15}' + titles[i].text)
        else:
            print(f'{i - 3}' + titles[i].text)
