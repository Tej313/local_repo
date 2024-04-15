from bs4 import BeautifulSoup
import requests 
from collections import Counter
import re

# Function to extract phrases from text
def extract_phrases(text):
    # Use regular expression to split text into phrases
    phrases = re.findall(r'\b\w+\s\w+\b', text)
    return [phrase.lower() for phrase in phrases]

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(html_text.text, 'html.parser')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# List to store all skills mentioned in the job descriptions
all_skills = []

for job in jobs:
    skills = job.find('span', class_='srp-skills').text.strip()
    all_skills.extend(extract_phrases(skills))

# Counting the frequency of each skill
skill_counter = Counter(all_skills)

# Extracting the top 10 most common skills
top_skills = skill_counter.most_common(10)

print('Top 10 phrases in job descriptions:')
for skill, frequency in top_skills:
    print(f"{skill}: {frequency}")
