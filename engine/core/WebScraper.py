import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from shutil import which

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
        # cProfile = wd.FirefoxProfile()
        options = Options()
        # options.profile = cProfile
        # options.binary = which("firefox")
        # options.headless = True
        
        for argument in arguments:
            options.add_argument(argument)
        
        return options
    
    def instantiateDriver(self, options):
        # cap = DesiredCapabilities().FIREFOX
        # cap["marionette"] = True
        driver = wd.Chrome("./chromedriver/cd", options=options)
        # driver = wd.Firefox(options=options)
        # driver = wd.Chrome(options=options)
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
    
    def getContent(self, url):
        content = ""
        tries = 0
        print(url)

        # while (len(content) == 0):
            # print(tries)
            # print(content)

            # if (tries != 0):
            #     time.sleep(10)
            
            # if (tries >= 10):
            #     raise Exception("# of tries exceeded 10")
            # else:
            #     print(15)
            #     try:
            #         print(1)
            #         driver.get(url)
            #         print(2)
            #         content = driver.page_source
            #         print(3)
            #         tries += 1
            #         print(4)
            #     except Exception as err:
            #         print(err)
            #         tries += 1
        
        while content == "":
            print(tries)
            options = self.createOptions(['-headless', '-no-sandbox'])
            driver = self.instantiateDriver(options)
            driver.get(url)
            time.sleep(5)
            content = driver.page_source
            print(content)
            tries += 1
            driver.quit()

        
        return content
