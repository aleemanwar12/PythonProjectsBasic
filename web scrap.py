from bs4 import BeautifulSoup
import requests
import time

print("Put A Skill which you are good in")
skills_of_user = input("> ")
print("filtering out jobs that require your skills")
print(".")
print("..")
print("...")
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        publish_date = job.find('span', class_='sim-posted').span.text

        if publish_date.lower() == 'posted few days ago' or 'posted today':
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills_req = job.find('span', class_='srp-skills').text.replace(" ", '')
            job_link = job.header.h2.a['href']
            if skills_of_user in skills_req:
                print(f'''
                Company Name: {company_name}
                skills required: {skills_req}
                Job Link: {job_link}
                ''')
                print("")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = (10)
        print(f'waiting for next {time_wait} minutes')
        time.sleep(time_wait*60)