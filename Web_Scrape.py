from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# To get the first <title> element on the html file
title_tag = doc.title.string

# To change the first <title> element in the html file
title_tag.string = "hello"
# Now, the html file will have "hello" as its <title> instead of what was previously there

# To find all <p> elements on the html file
p_tags = doc.find_all("p")

# To find certain text
text_words = doc.find_all(text="certain_word")

# To extract the parent element of the certain text
parent = text_words[0].parent

# To search websites
import requests
url = "https://www.congress.gov/bill/118th-congress/house-bill/2670/all-actions?q=%7B%22roll-call-vote%22%3A%22all%22%2C%22action-by%22%3A%22Senate%22%7D"
result = requests.get(url)

# To extract the html from the url (doesn't work on all websites due to anti-bot measures)
doc = BeautifulSoup(result.text, "html.parser")

# Printing out the webpage
print(doc.prettify())
