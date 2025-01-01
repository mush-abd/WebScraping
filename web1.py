import requests
from bs4 import BeautifulSoup

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='

search_result = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

website = BeautifulSoup(search_result, 'html.parser')

jobs = website.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# print(jobs)

for job in jobs:

    company = job.find('h3', class_ = 'joblist-comp-name').text.replace('\n', '').replace('\t', '')
    # print(company)
    skills_list = job.find('div', class_ = 'srp-skills')
    skills = [span.get_text().replace('\n', '').replace('\t', '') for span in skills_list.find_all('span')]
    skills = ', '.join(skills)
    skills = skills.replace('   ,', ',').replace('  ,', ',').replace(',   ', ',')
    published_date = job.find('span', class_ = 'sim-posted').span.text
    link = job.header.h2.a['href']
    # print(published_date)
    # print(skills)

    if published_date == 'few days ago':
        print(f'''
    
        Company : {company}
        Skills : {skills}
        Link : {link}
        ''')
# print(website)