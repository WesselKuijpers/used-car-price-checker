import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from shutil import which

class WebScraper:
    def __init__(self, base_url, sub_urls, url_params, *args):
        self.__chrome_arguments = args
        self.__base_url = base_url
        self.__sub_urls = sub_urls
        self.__url_params = url_params
        self.__url = ""
        self.__content = ""
        self.__driver = None
        self.__chrome_options = Options()

        self.__scrape()

    @property
    def content(self):
        if (self.__content != ""): 
            return self.__content
        else:
            return Exception("Content is empty!")

    def __scrape(self):
        self.__create_options()
        self.__instantiate_driver()
        self.__build_link()
        self.__get_content()

    def __create_options(self):
        for argument in self.__chrome_arguments:
            self.__chrome_options.add_argument(argument)
    
    def __instantiate_driver(self):
        self.__driver = wd.Chrome(executable_path="/usr/bin/chromedriver", options=self.__chrome_options)
    
    def __build_link(self):
        if (len(self.__sub_urls) != 0):
            for sub_url in self.__sub_urls:
                if (sub_url[0] != '/'):
                    self.__url += '/'
                self.__url += sub_url
        
        if (len(self.__url_params) != 0):
            self.__url += '/'
            for k,v in self.__url_params.items():
                self.__url += '?' + k
                self.__url += '=' + v
    
    def __get_content(self):
        tries = 0

        while self.__content == "":
            self.__driver.get(self.__url)
            time.sleep(5)
            self.content = self.__driver.page_source
            tries += 1
            self.__driver.quit()

