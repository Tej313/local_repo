from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

# Specify the parser explicitly as 'html.parser' in quotes
soup = BeautifulSoup(page.content, 'html.parser')

# Print the title of the page
print(soup.prettify)

