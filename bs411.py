import requests 
from bs4 import BeautifulSoup as bs 

URLs = ['https://www.geeksforgeeks.org', 'https://www.geeksforgeeks.org/page/10/']

for url in URLs:
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class': 'head'})

    try:
        page_number = int(url.split("/")[-1])
    except ValueError:
        page_number = None

    for i in range(4, min(19, len(titles))):  
        if page_number is not None:
            print(f'{(i - 3) + (page_number - 1) * 15}' + titles[i].text)
        else:
            print(f'{i - 3}' + titles[i].text)


