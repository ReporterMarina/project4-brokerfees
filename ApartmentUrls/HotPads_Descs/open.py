from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests  # Import the requests library
from selenium.webdriver.chrome.options import Options
import chromedriver_binary # adds the chromedriver binary to the path

# Configure ChromeOptions for the regular browser instance
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

url = "https://www.example.com"
driver.get(url)