import requests
import csv
from bs4 import BeautifulSoup
#link to be scraped
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Engineer&txtLocation=new+york').text
#creating a object variable for beautiful
header=['company_name','skill','date_posted','link_to_job']
soup=BeautifulSoup(html_text,'lxml')
job=soup.find_all('li',class_='clearfix job-bx wht-shd-bx') #class is used to specify the specific class of li tag we want to retrive
for index,jobs in enumerate(job):
        company_name=jobs.find('h3', class_='joblist-comp-name').text.replace(' ','')
        skills=jobs.find('span',class_='srp-skills').text.replace(' ','')
        posted_date=jobs.find('span', class_='sim-posted').span.text
        more_info=jobs.header.h2.a['href']
        data=[company_name,skills,posted_date,more_info]
        with open(f'/Volumes/PortableSSD/TestScraping/LiveScrapping/posts/{index}.txt','w') as f: #file being saved to location
            f.write(company_name.strip()+'\n'+skills.strip()+'\n'+posted_date.strip()+'\n'+more_info.strip())
print("File Save")
            