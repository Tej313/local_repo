import requests
from bs4 import BeautifulSoup
import json

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    job_listings = []

    for job_card in soup.find_all('li', class_='clearfix job-bx wht-shd-bx'):
        job_title = job_card.find('h2').text.strip()
        company_name = job_card.find('h3', class_='joblist-comp-name').text.strip()
        skills_required = job_card.find('span', class_='srp-skills').text.strip()
        experience_required = job_card.find('ul', class_='top-jd-dtl clearfix').find('li').text.strip()

        job_info = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Skills Required': skills_required,
            'Experience Required': experience_required
        }

        job_listings.append(job_info)

    return job_listings

if __name__ == "__main__":
    programming_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=programming&txtLocation="
    marketing_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=marketing&txtLocation="

    programming_jobs = scrape_jobs(programming_url)
    marketing_jobs = scrape_jobs(marketing_url)

    with open("programming.json", 'w', encoding='utf-8') as programming_file:
        json.dump(programming_jobs, programming_file, ensure_ascii=False, indent=2)

    with open("marketing.json", 'w', encoding='utf-8') as marketing_file:
        json.dump(marketing_jobs, marketing_file, ensure_ascii=False, indent=2)
