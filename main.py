from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By

html_text = requests.get('https://www.glassdoor.com/Job/hong-kong-python-developer-jobs-SRCH_IL.0,9_IC2308631_KO10,26.htm?sortBy=date_desc').text
soup = BeautifulSoup(html_text, 'lxml')

url = 'https://www.glassdoor.com/Job/hong-kong-python-developer-jobs-SRCH_IL.0,9_IC2308631_KO10,26.htm?sortBy=date_desc'
driver = webdriver.Chrome('Users/almonsubba/Downloads/chromedriver')
driver.get(url)

# Find company name(s).
job = soup.find('li', class_ = 'react-job-listing css-wp148e eigr9kq4')
company_name = job.find('a', class_ = 'css-l2wjgv e1n63ojh0 jobLink').text

# Find job requirements. (Python)
for skills in driver.find_elements(By.XPATH, '//div[@class="jobDescriptionContent desc"]'):
    print(skills.text)

# print(f'Company Name: {company_name},\nRequired Skills: {skills}')
