from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time 
import pandas as pd
from sklearn.datasets import load_iris


def python_jobs(num_jobs, check):
    '''Gets jobs for 'python developer' as a dataframe from Glassdoor.'''

    url = 'https://www.glassdoor.com/Job/hong-kong-python-developer-jobs-SRCH_IL.0,9_IC2308631_KO10,26.htm?sortBy=date_desc'
    driver = webdriver.Chrome('Users/almonsubba/Downloads/chromedriver')
    driver.get(url)
    
    jobs = []

    # If its true, will still be looking for jobs.
    while len(jobs) < num_jobs:

        time.sleep(5)

        # Close sign up prompt pop up.
        try:
            driver.find_element(By.CLASS_NAME, 'SVGInline-svg modal_closeIcon-svg').click()
        except NoSuchElementException:
            pass

        time.sleep(1)

        # Expand description by clicking See More.
        try:
            driver.find_element(By.CSS_SELECTOR, 'css-t3xrds e856ufb4').click()
        except NoSuchElementException:
            pass


        # Clicking each job card button.
        job_buttons = driver.find_elements(By.XPATH, "//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")
        for job_button in job_buttons:
            
            print("Loading...")
            if len(jobs) >= num_jobs:
                break

            try:
                job_button.click()
                time.sleep(1)
                collected_successfully = False
            except ElementClickInterceptedException:
                pass
            
            # Keeps searching unless.
            while not collected_successfully:
                try:
                    company_name = driver.find_element(By.XPATH, './/div[@class="css-87uc0g e1tk4kwz1"]').text
                    job_title = driver.find_element(By.XPATH, './/div[@class="css-1vg6q84 e1tk4kwz4"]').text
                    job_description = driver.find_element(By.XPATH, './/div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            if check:
                print("Job Title: {}".format(job_title))
                print("Company Name: {}".format(company_name))
                print("Job Description: {}".format(job_description))

            jobs.append({"Job Title" : job_title,
            "Company Name" : company_name,
            "Job Description" : job_description})

        try:
            driver.find_element(By.CLASS_NAME, 'SVGInline-svg navIcon-svg css-g9i05x-svg e13qs2073-svg').click()
        except NoSuchElementException:
            print("Scraping terminated because reached limit.")
            break

    return pd.DataFrame(jobs)

df = python_jobs(5, False)
print(df.to_string())