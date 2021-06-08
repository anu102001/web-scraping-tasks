from bs4 import  BeautifulSoup

import requests
import time

print('put some skill that you are not familiar with')
unf_skills = input('>')
print(f'filtering out {unf_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchName=recentSearches&from=submit&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&gadLink=Python').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_ ='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
      job_pdate=job.find('span', class_='sim-posted').span.text
      if 'few' in job_pdate:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span', class_='srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        if unf_skills not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name:{company_name.strip()} \n")
                f.write(f"required skills:{skills.strip()} \n")
                f.write(f'more_info:{more_info}')
            print(f'file saved in index:{index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait= 10
        print(f'waiting {time_wait} seconds.....')
        time.sleep(time_wait* 60)
         