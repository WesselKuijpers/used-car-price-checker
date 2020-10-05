import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import time

class WebScraper:
    chrome_arguments = []
    chrome_options = None
    baseUrl = ""
    subUrls = []
    params = {}
    driver = None
    url = ""
    content = None

    def scrape(self):
        #
        return

    def createOptions(self, arguments=[]):
        chrome_options = Options()
        
        for argument in arguments:
            chrome_options.add_argument(argument)
        
        return chrome_options
    
    def instantiateDriver(self, chrome_options):
        driver = wd.Chrome("./chromedriver/cd", options=chrome_options)
        return driver
    
    def buildLink(self, baseUrl, subUrls = [], params={}):
        url = baseUrl

        if (len(subUrls) != 0):
            for subUrl in subUrls:
                if (subUrl[0] != '/'):
                    url += '/'
                url += subUrl
        
        if (len(params) != 0):
            print(params)
            url += '/'
            for k,v in params.items():
                url += '?' + k
                url += '=' + v

        return url
    
    def getContent(self, driver, url):
        content = ""
        tries = 0
        print(url)

        while (len(content) == 0):
            print(tries)
            print(content)

            if (tries != 0):
                time.sleep(10)
            
            if (tries >= 10):
                raise Exception("# of tries exceeded 10")
            else:
                print(15)
                try:
                    print(1)
                    driver.get(url)
                    print(2)
                    content = driver.page_source
                    print(3)
                    tries += 1
                    print(4)
                except Exception as err:
                    print(err)
                    tries += 1
                
        
        driver.quit()
        
        return content
