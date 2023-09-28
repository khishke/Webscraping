from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = Options()

driver = webdriver.Chrome(options=options)

url ="https://www.zangia.mn/"
driver.get(url)

zangia_main_page = "https://www.zangia.mn/"
webdriver.get(zangia_main_page)
driver.find_element(By.XPATH, "/html/body/div[1]/div/form/input[1]").send_keys("Дата аналист")
driver.find_element(By.XPATH, "/html/body/div[1]/div/form/input[2]").send_keys(Keys.ENTER) 

#Loop#

html_xpath = '/html/body/div[2]/div[1]/div/div[3]/div/div[3]/div' 
custom_xpath = f"By.XPATH, '{html_xpath}'"
elements = driver.find_elements(*eval(custom_xpath))
list_jobs= []

for element in elements:
    try:
        salary_element = element.find_element(By.XPATH, "./*[@class='specific-class']/a/span[1]")   ##path /html/body/div[2]/div[1]/div/div[3]/div/div[3]/div[1]/div[2]/a/span[1]; /html/body/div[2]/div[1]/div/div[3]/div/div[3]/div[2]/div[2]/a/span[1]
        salary = salary_element.text
        list_jobs.append(salary)
    except NoSuchElementException:
        list_jobs.append("Element not found")