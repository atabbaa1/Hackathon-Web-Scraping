from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

############################################     Opening up the webpage      ###########################################################

# Retrieving the website
url = "https://www.congress.gov/bill/118th-congress/house-bill/2670"
driver.get(url)

# Keep website open for 5 seconds
time.sleep(5)

# Close webpage
driver.quit()

###############################     Searching for and Interacting with elements in html      ###########################################

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# finding the first element by class name
input_element = driver.find_element(By.CLASS_NAME, "some_class_name")
# to extract just the text from the element, append .text to the end
input_element_text = driver.find_element(By.CLASS_NAME, "some_class_name").text

# finding the first element by id
input_element = driver.find_element(By.ID, "some_id")

# For finding elements with general searches like contains -----, use XPATH. Use chatGPT to determien the syntax for XPATH
input_element = driver.find_element(By.XPATH, "some XPATH expression which may not be a string")

# Sending keys into elements
input_element.send_keys("some random string in a text search" + Keys.ENTER)

# Clearing elements. Useful for text areas
input_element.clear()

# Wait 5s for an element to load
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "some_class_name")))

# Searching for first element based on partial text
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Some random partial text")
#Clicking on link
link.click()
