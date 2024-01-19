import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Scrape job listings and save to JSON file.')
    parser.add_argument('category', choices=['programming', 'marketing'], help='Specify the job category')

    args = parser.parse_args()

    if args.category == 'programming':
        url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=programming&txtLocation="
    elif args.category == 'marketing':
        url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=marketing&txtLocation="
    else:
        print("Invalid category. Choose either 'programming' or 'marketing'.")
        return

    jobs = scrape_jobs(url)

    with open(f"{args.category}.json", 'w', encoding='utf-8') as file:
        json.dump(jobs, file, ensure_ascii=False, indent=2)
    print(f"Job listings for {args.category} saved to {args.category}.json")

if __name__ == "__main__":
    import sys
    sys.argv = [sys.argv[0]] + ['/Users/tej/Documents/visual studio/local_repo/pythonjobs12.py', 'programming']
    main()
