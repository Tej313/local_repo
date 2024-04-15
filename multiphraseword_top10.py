from bs4 import BeautifulSoup
import requests 
from collections import Counter
import re

# Function to extract keywords from text
def extract_keywords(text):
    # Use regular expression to split text into phrases and single words
    keywords = re.findall(r'\b\w+\b|\b\w+\s\w+\b', text)
    return [keyword.lower() for keyword in keywords]

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(html_text.text, 'html.parser')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# List to store all keywords mentioned in the job descriptions
all_keywords = []

for job in jobs:
    skills = job.find('span', class_='srp-skills').text.strip()
    all_keywords.extend(extract_keywords(skills))

# Counting the frequency of each keyword
keyword_counter = Counter(all_keywords)

# Extracting the top 10 most common keywords
top_keywords = keyword_counter.most_common(10)

print('Top 10 keywords in job descriptions:')
for keyword, frequency in top_keywords:
    print(f"{keyword}: {frequency}")
