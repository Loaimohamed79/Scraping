import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jop_title = []
company = []
skills = []
location = []
links = []
salary = []
job_Req = []


url = ("https://wuzzuf.net/search/jobs/?a=hpb&q=data%20analysis&start=")
for page in range(44):
    result= requests.get(url + str(page))
    print(page)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    jop_titles = soup.find_all("h2", {"class": "css-m604qf"})
    company_names = soup.find_all("a", {"class": "css-17s97q8"})
    loaction_company = soup.find_all("span", {"class": "css-5wys0k"})
    jop_skills = soup.find_all("div", {"class": "css-y4udm8"})

    for i in range(len(jop_titles)):
        jop_title.append(jop_titles[i].text)
        links.append(jop_titles[i].find("a").attrs["href"])
        company.append(company_names[i].text)
        location.append(loaction_company[i].text)
        skills.append(jop_skills[i].text)

    for link in links:
        result = requests.get(link) 
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        # job_requirements = soup.find("div", {"class": "css-1t5f0fr"}).find("ul")
        # respon_txt = " "
    
#     for li in job_requirements.find_all("li"):
#         respon_txt += li.text + " | "

#     respon_txt = respon_txt[:-2]
#     job_Req.append(respon_txt)

    file_list = [jop_title, company, location, skills, links]
    exported = zip_longest(*file_list)

    with open("D:\TTT.csv", "w",encoding='utf8') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(["Jop title", "Company name",
                "Location", "Skills", "links"])
        wr.writerows(exported)
