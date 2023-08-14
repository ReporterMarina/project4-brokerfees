from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import os

# Initialize the Chrome driver
driver = webdriver.Chrome()

def open_browser():
    """
    Opens a new automated browser window with all tell-tales of automated browser disabled
    """
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    # remove all signs of this being an automated browser
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # open the browser with the new options
    driver = webdriver.Chrome(options=options)
    return driver

# Open the URL
url = "https://www.zillow.com/boston-ma/rentals/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Boston%20MA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-71.30134051513673%2C%22east%22%3A-70.79390948486329%2C%22south%22%3A42.175170418497544%2C%22north%22%3A42.451389648714844%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A44269%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22doz%22%3A%7B%22value%22%3A%2214%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
driver.get(url)

# # Use WebDriverWait to wait until listing URLs are loaded
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.list-card-link")))

# Get the page source after loading all listings
page_source = driver.page_source

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, "html.parser")

# Find all listing URLs
listing_links = soup.find_all("a", class_="list-card-link")

# Extract and store URLs in a list
listing_urls = [link["href"] for link in listing_links]

# Define the path to the Desktop directory
desktop_path = os.path.expanduser("~/Desktop")

# Save URLs to a CSV file on the Desktop
csv_filename = os.path.join(desktop_path, "zillow_listing_urls.csv")
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["URL"])

    # Write each listing URL to the CSV file
    for url in listing_urls:
        csv_writer.writerow([url])

# Close the browser
driver.quit()
