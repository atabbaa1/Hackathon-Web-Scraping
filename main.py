from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Open_AI_Custom_Chatbot.MainCode import WiseSage
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

pg_load_time = 3

############################################     Opening up the webpage      ###########################################################

# Retrieving the website
url = "https://www.congress.gov/bill/118th-congress/house-bill/7024"
driver.get(url)


"""
############################################     Viewing Congressmen votes   ###########################################################
WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.CLASS_NAME, "overview")))

# Check and ensure there has been a roll call vote
roll_call_link = driver.find_element(By.XPATH, "//*[@class='overview']//a[contains(text(), 'roll call')]")
if roll_call_link:
    # Move onto the next page
    roll_call_link.click()

WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.XPATH, "//table[thead//*[contains(text(), 'Chamber')] and thead//*[contains(text(), 'All Actions')]]")))

# Find the table with the progression of the bill
prog_table = driver.find_element(By.XPATH, "//table[thead//*[contains(text(), 'Chamber')] and thead//*[contains(text(), 'All Actions')]]")
# If the table is present, find the latest roll call vote
if prog_table:
    house_vote = prog_table.find_element(By.XPATH, ".//*[//[contains(text(), 'House')] and (.//a[contains(text(), 'roll')] or .//a[contains(text(), 'vote')])]")
    house_link = prog_table.find_element(By.XPATH, ".//a[contains(text(), 'roll')] or .//a[contains(text(), 'vote')]")
    # Move onto the next page
    house_link.click()

time.sleep(pg_load_time)
"""
# eventually,
# with open("Open_AI_Custom_Chatbot/data/vote_table.html", "w") as text_file:
    # text_file.write(WebElement.get_attribute("innerHTML"))
# text_file.close()




############################################     Summarizing the bill        ###########################################################
WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.ID, "bill-summary")))

# Getting the text summary
bill_summary = driver.find_element(By.ID, "bill-summary").text

# Exporting the text as a .txt file to a location where the GPT model will be able to interact with it
with open("Open_AI_Custom_Chatbot/data/bill_summary.txt", "w") as text_file:
    text_file.write(bill_summary)

# Closing the new .txt file
text_file.close()




############################################     Closing the webpage      ###########################################################
driver.quit()



###########################################       Calling LLM function         ####################################################
llm_summarizer = WiseSage()
llm_summarizer.main("Open_AI_Custom_Chatbot" + "\\")