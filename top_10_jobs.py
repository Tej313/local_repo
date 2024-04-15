from bs4 import BeautifulSoup
import requests 
from collections import Counter

# Function to extract keywords from text
def extract_keywords(text):
    return [word.lower() for word in text.split()]

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(html_text.text, 'html.parser')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# List to store all skills mentioned in the job descriptions
all_skills = []

for job in jobs:
    skills = job.find('span', class_='srp-skills').text.strip()
    all_skills.extend(extract_keywords(skills))

# Counting the frequency of each skill
skill_counter = Counter(all_skills)

# Extracting the top 10 most common skills
top_skills = skill_counter.most_common(10)

print('Top 10 keywords in job descriptions:')
for skill, frequency in top_skills:
    print(f"{skill}: {frequency}")
