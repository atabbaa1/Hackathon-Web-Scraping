from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

pg_load_time = 3

############################################     Opening up the webpage      ###########################################################

# Retrieving the website
url = "https://www.congress.gov/bill/118th-congress/house-bill/2670"
driver.get(url)

############################################     Viewing Congressmen votes   ###########################################################




############################################     Summarizing the bill        ###########################################################
WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.CLASS_NAME, "bill-summary")))
bill_summary = driver.find_element(By.CLASS_NAME, "bill-summary").text




############################################     Closing the webpage      ###########################################################
driver.quit()