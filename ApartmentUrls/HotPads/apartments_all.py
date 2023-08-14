import os
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Initialize the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

# Desktop path (update this with your actual path)
desktop_path = os.path.expanduser("~/Desktop")

# Open each page and scrape URLs
for page_number in range(305, 405):  # Page range 1 to 231
    page_url = f"https://hotpads.com/cambridge-ma/apartments-for-rent?border=false&lat=42.3674&lon=-71.1054&maxCreated=720&page={page_number}"
    driver.get(page_url)

    # Introduce a time delay of 2 seconds before proceeding to the next page
    time.sleep(2)  # Adjust the delay time as needed

    # Get the page source after loading all listings
    page_source = driver.page_source

    # Parse the page source with Beautiful Soup
    soup = BeautifulSoup(page_source, "html.parser")

    # Find all listing URLs within <a> tags
    listing_links = soup.find_all("a")

    # Extract and store URLs in a list
    listing_urls = [link["href"] for link in listing_links]

    # Save URLs to a CSV file for each page
    csv_filename = os.path.join(desktop_path, f"recent_apartment_urls_page_{page_number}.csv")
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["URL"])

        # Write each listing URL to the CSV file
        for url in listing_urls:
            csv_writer.writerow([url])

# Close the browser
driver.quit()
