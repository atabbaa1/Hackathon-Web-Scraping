This is our web scraping project.

To use Selenium, you will need to install it with the following command:
`pip install selenium`

If that doesn't work, try the following commands:   
`pip3 install beautifulsoup4` or  
`python -m pip install beautifulsoup4` or  
`python3 -m pip install beautifulsoup4`

Update your Chrome browser to the latest version. At this point, it should be 127.X.XXXX.XX

Navigate to [this page](https://sites.google.com/chromium.org/driver). Then, click on the 3rd link from the top which says [the Chrome for Testing Availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/). Download the stable Chrome web driver associated with your operating system. MAKE SURE YOU DOWNLOAD chromedriver NOT chrome!

After downloading the web driver and extracting the files, locate the chromedriver.exe file. Copy it into the same directory the Python file is at.

**OPTIONAL**: Check out [Bright Data](https://brightdata.com/products/scraping-browser?utm_source=brand&utm_campaign=brnd-mkt_youtube_techwithtim_selenium&promo=techwithtim) later on for Web Scraping at large to avoid Captchas and getting blocked.  

Open a terminal and navigate to the directory  
    $...\Open_AI_Custom_Chatbot>  

Type in the command:
    `pip install pipenv`  
    Pipenv will be used to install compatible versions of python packages and sub-dependencies using the pipfile and pipfile.lock  

Install python dependencies using the command:  
    `pipenv install --ignore-pipfile`  

(Optional) Spawn a shell in a virtual environment by typing in the command:  
    `pipenv shell`  
While in the virtual environment, you can leave using the command:  
    `exit`  
Do NOT use the command deactiviate, as this may not actually exit the virtual environment.  

Open MainCode.py and insert your OPEN_API_KEY on the first line.  

