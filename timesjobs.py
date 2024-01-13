from bs4 import BeautifulSoup
import requests 
import time
import os  # Import the os module

def find_jobs():
    print('put some skills you are not familiar with')
    unfamilir_skill = input('>')
    print(f"filtering out {unfamilir_skill}")
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(html_text.text, 'html.parser')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    # Create 'posts' directory if it doesn't exist
    os.makedirs('posts', exist_ok=True)
    
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            
            if unfamilir_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'company name : {company_name.strip()}\n')
                    f.write(f'skills : {skills.strip()}\n')
                    f.write(f'more info : {more_info}\n')
                
                print(f'file saved : {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
