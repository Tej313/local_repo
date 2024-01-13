from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()  # Corrected: Added parentheses to call the read method
    soup = BeautifulSoup(content, 'html.parser')  # Create a BeautifulSoup object
    print(soup.prettify())
