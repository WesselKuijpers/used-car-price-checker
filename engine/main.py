import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import time

brandsModels = []
types = []
prices = []

content = ""
tries = 0

try:
    while (len(content) == 0):
        print(tries)
        if (tries > 0):
            time.sleep(10)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.headless = True
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = wd.Chrome("./chromedriver/cd", options=chrome_options)

        driver.get("https://www.autowereld.nl/saab/?mdl=saab_900|saab_900-cabrio|saab_900-coupe")
        content = driver.page_source
        driver.quit()
        tries += 1
except:
    driver.quit()

print(len(content))

soup = bs(content, features="html.parser")

for article in soup.findAll('article', attrs={'class': 'item'}):
    frame = article.find('a', href=True, attrs={'class': 'frame'})
    cellInfo = frame.find('div', attrs={'class': 'cell info'})
    cellInfoBox = cellInfo.find('div', attrs={'class': 'box'})
    cellInfoBoxTitle = cellInfoBox.find('h3', attrs={'class': 'title'})

    brandsModels.append(cellInfoBoxTitle.find('span', attrs={'class': 'brandmodel'}).text)

    carType = cellInfoBoxTitle.find('span', attrs={'class': 'type'})
    if (carType != None):
        types.append(carType.text)

    cellInfoBasicSpecsButton1 = cellInfo.find('div', attrs={'class': 'basic-specs button-1'})
    cellInfoBasicSpecsButton1Content = cellInfoBasicSpecsButton1.find('div', attrs={'class': 'content'})

    prices.append(cellInfoBasicSpecsButton1Content.find('div', attrs={'class': 'price'}).text)

print(brandsModels)
print(types)
print(prices)

    

