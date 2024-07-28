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

pg_load_time = 5

############################################     Opening up the webpage      ###########################################################

# Retrieving the website
url = "https://www.congress.gov/bill/118th-congress/house-bill/7024" # Shorter bill
# url = "https://www.congress.gov/bill/118th-congress/house-bill/2670" # longer bill
driver.get(url)

############################################     Summarizing the bill        ###########################################################
WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.ID, "bill-summary")))

# Getting the text summary
bill_summary = driver.find_element(By.ID, "bill-summary")
bill_summary_string = bill_summary.text

# Exporting the text as a .txt file to a location where the GPT model will be able to interact with it
with open("Open_AI_Custom_Chatbot/data/bill_summary.txt", "w") as text_file:
    text_file.write(bill_summary_string)

# Extracting the name of the bill
bill_name = bill_summary.find_element(By.XPATH, "./p").text

# Closing the new .txt file
text_file.close()


############################################     Viewing Congressmen votes   ###########################################################
WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.CLASS_NAME, "overview")))

# Check and ensure there has been a roll call vote
roll_call_link = driver.find_element(By.XPATH, "//*[@class='overview']//a[contains(text(), 'roll call')]")
if roll_call_link:
    # Move onto the next page
    roll_call_link.click()

WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.XPATH, "//table[thead//*[contains(text(), 'All Actions')]]")))

# Find the table with the progression of the bill
prog_table = driver.find_element(By.XPATH, "//table[thead//*[contains(text(), 'All Actions')]]")

# If the table is present, find the latest roll call vote for the House
if prog_table:
    house_row = prog_table.find_element(By.XPATH, ".//tr[td//a[contains(text(), 'Roll')]]")
    house_link = house_row.find_element(By.XPATH, ".//a[contains(text(), 'Roll')]")

    # Scroll down to the link
    html_element = driver.find_element(By.TAG_NAME, "html")
    html_element.send_keys(Keys.DOWN)
    html_element.send_keys(Keys.DOWN)
    html_element.send_keys(Keys.DOWN)
    html_element.send_keys(Keys.DOWN)
    html_element.send_keys(Keys.DOWN)
    html_element.send_keys(Keys.DOWN)
    
    # Move onto the next page. It opens in a new tab, so I need to switch tabs.
    house_link.click()
    time.sleep(pg_load_time)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])

    WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.CLASS_NAME, "table-responsive")))
    # Get the tables
    tables = driver.find_elements(By.CLASS_NAME, "table-responsive")

    # Exporting the first table which is just overall parties
    with open("Open_AI_Custom_Chatbot/data/by_party_table.html", "w") as party_table:
        party_table.write(tables[0].get_attribute("innerHTML"))
    party_table.close()

    # Exporting the second table which is each individual candidate
    with open("Open_AI_Custom_Chatbot/data/by_candidate_table.html", "w") as candidate_table:
        candidate_table.write(tables[1].get_attribute("innerHTML"))
    candidate_table.close()

    # Go back to the previous tab.
    driver.switch_to.window(window_handles[0])
    # Then, go back to the page with the prog_table to extract info for senators
    driver.back()

    """                INFORMATION FOR SENATORS. NEVER GOT IMPLEMENTED IN TIME
    WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.XPATH, "//table[thead//*[contains(text(), 'Chamber')] and thead//*[contains(text(), 'All Actions')]]")))
    senate_row = driver.find_element(By.XPATH, ".//tr[td[contains(text(), 'Senate')] and td//a[contains(text(), 'Vote')]]")
    senate_link = house_row.find_element(By.XPATH, ".//a[contains(text(), 'Vote')]")
    # Just because the House has voted, doesn't mean the Senate has also voted
    if senate_row:

        # Scroll down to the link
        html_element = driver.find_element(By.TAG_NAME, "html")
        html_element.send_keys(Keys.DOWN)
        html_element.send_keys(Keys.DOWN)
        html_element.send_keys(Keys.DOWN)
        html_element.send_keys(Keys.DOWN)
        html_element.send_keys(Keys.DOWN)
        html_element.send_keys(Keys.DOWN)
    
        # Move onto the next page
        senate_link.click()

        # WebDriverWait(driver, pg_load_time).until(EC.presence_of_element_located((By.CLASS_NAME, "newspaperDisplay_3column")))
        # Get the table
    """



############################################     Closing the webpage      ###########################################################
driver.quit()



###########################################       Calling LLM function         ####################################################
# llm_summarizer = WiseSage()
# llm_summarizer.main("Open_AI_Custom_Chatbot" + "\\", bill_name)