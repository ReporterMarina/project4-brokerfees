from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import os

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL
url = "https://www.apartments.com/boston-ma/?bb=pwn4qnsurHthrt01H"
driver.get(url)

# Use WebDriverWait to wait until listing URLs are loaded
# wait = WebDriverWait(driver, 20)
# wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.srp-item a.property-link")))

# Get the page source after loading all listings
page_source = driver.page_source

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, "html.parser")

# Find all listing URLs
listing_links = soup.find_all("a", class_="property-link")

# Extract and store URLs in a list
listing_urls = [link["href"] for link in listing_links]

# Define the path to the Desktop directory
desktop_path = os.path.expanduser("~/Desktop")

# Save URLs to a CSV file on the Desktop
csv_filename = os.path.join(desktop_path, "apartment_urls.csv")
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["URL"])

    # Write each listing URL to the CSV file
    for url in listing_urls:
        csv_writer.writerow([url])

# Close the browser
driver.quit()
