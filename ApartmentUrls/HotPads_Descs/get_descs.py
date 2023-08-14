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

# # Initialize the Chrome driver
# driver = webdriver.Chrome()

# # Initialize Chrome WebDriver in headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# headless_driver = webdriver.Chrome(options=chrome_options)


# Create a list of example URLs
urls = [
"https://www.hotpads.com/33-portsmouth-st-cambridge-ma-02141-spm533/r3/pad",
"https://www.hotpads.com/4-centre-st-roxbury-ma-02119-skkb2n/6/pad",
"https://www.hotpads.com/854-beacon-st-boston-ma-02215-skemhr/a/pad",
"https://www.hotpads.com/171-south-st-boston-ma-02130-skg49c/5a/pad",
"https://www.hotpads.com/391-harvard-st-brookline-ma-02446-1zns6pt/2/pad",
"https://www.hotpads.com/12-follen-st-boston-ma-02116-skffzb/p1/pad",
"https://www.hotpads.com/200-w-7th-st-south-boston-ma-02127-1w45jv0/pad",
"https://www.hotpads.com/208-w-7th-st-south-boston-ma-02127-spw5c0/2/pad",
"https://www.hotpads.com/85-revere-st-boston-ma-02114-skeq2k/1a/pad",
"https://www.hotpads.com/40-hooker-st-allston-ma-02134-skgv7k/1e/pad",
"https://www.hotpads.com/174-bay-state-rd-boston-ma-02215-skepwf/2r/pad",
"https://www.hotpads.com/460-470-beacon-st-boston-ma-02215-23a3fya/4b/pad",
"https://www.hotpads.com/61-66-brookline-ave-boston-ma-02215-23a3fy5/221a/pad",
"https://www.hotpads.com/471-475-commonwealth-ave-boston-ma-02215-23a3fym/pad",
"https://www.hotpads.com/160-165-newbury-st-boston-ma-02116-23a3fyh/2a/pad",
"https://www.hotpads.com/59-61-brookline-ave-boston-ma-02215-23a4cyb/313/pad",
"https://www.hotpads.com/132-140-highland-ave-somerville-ma-02143-23a48a4/18/pad",
"https://www.hotpads.com/112-114-2nd-st-cambridge-ma-02141-23a48a2/9b/pad",
"https://www.hotpads.com/6-castleton-st-boston-ma-02130-thjq97/2/pad",
"https://www.hotpads.com/103-buttonwood-st-boston-ma-02125-1j4qm8e/3/pad",
"https://www.hotpads.com/7-sudan-st-boston-ma-02125-w1nbj3/1/pad",
"https://www.hotpads.com/1238-commonwealth-ave-allston-ma-02134-skyex8/42/pad",
"https://www.hotpads.com/69-springfield-st-somerville-ma-02143-uuhmc2/1/pad",
"https://www.hotpads.com/piano-craft-guild-boston-ma-02118-skedwt/pad",
"https://www.hotpads.com/9-brown-st-waltham-ma-02453-1j570t0/9/pad",
"https://www.hotpads.com/394-centre-st-boston-ma-02130-th2pp5/3/pad",
"https://www.hotpads.com/29-gloucester-st-boston-ma-02116-1n7unft/3/pad",
"https://www.hotpads.com/186-saint-botolph-st-boston-ma-02115-tnu642/pad",
"https://www.hotpads.com/29-bentley-st-boston-ma-02135-upqru4/sf/pad",
"https://www.hotpads.com/10-copeland-park-roxbury-ma-02119-1u66yqa/d/pad",
"https://www.hotpads.com/402-centre-st-boston-ma-02130-utj10k/1/pad",
"https://www.hotpads.com/220-banks-st-cambridge-ma-02138-skeq8r/4/pad",
"https://www.hotpads.com/183-beacon-st-boston-ma-02116-skhj1t/1/pad-for-sublet",
"https://www.hotpads.com/185-saint-botolph-st-boston-ma-02115-skenhu/4/pad-for-sublet",
]


# Create an empty list to store extracted text
#extracted_text_list = []

# Define the path to the Desktop directory
desktop_path = os.path.expanduser("~/Desktop")

# Split the list of URLs into batches of 100
batch_size = 100
url_batches = [urls[i:i + batch_size] for i in range(0, len(urls), batch_size)]

for batch_index, url_batch in enumerate(url_batches):
    batch_index = 32
    print(f"Processing batch {batch_index}")
    
    # Create a list to store URLs that weren't processed
    urls_not_processed = []
    
    # Loop through the URLs in the current batch
    for url_index, url in enumerate(url_batch):
        try:
            print(f"Processing URL: {url}")

            # Open the URL
            driver.get(url)
            
            # Wait for elements to load
            driver.implicitly_wait(10)
            
            # Wait for the parent element to be present
            wait = WebDriverWait(driver, 10)
            parent_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles__DescriptionText-zqkn84-0.hUAYaq")))

            # Extract the text from the section element
            about_property_text = parent_element.text
            
            # Find the HdpSummaryDetails element
            summary_details_element = driver.find_element(By.CLASS_NAME, "HdpSummaryDetails")
            
            # Find elements within the summary_details_element
            rent_element = summary_details_element.find_element(By.XPATH, './/span[contains(text(), "Monthly Rent")]')
            beds_element = summary_details_element.find_element(By.XPATH, './/span[contains(text(), "Beds")]')
            baths_element = summary_details_element.find_element(By.XPATH, './/span[contains(text(), "Baths")]')
            
            # Extract the values from the elements
            monthly_rent = rent_element.find_element(By.XPATH, './preceding-sibling::span').text
            beds = beds_element.find_element(By.XPATH, './preceding-sibling::span').text
            baths = baths_element.find_element(By.XPATH, './preceding-sibling::span').text

            # Find the sqft element if it exists
            try:
                sqft_element = summary_details_element.find_element(By.XPATH, './/span[contains(text(), "Sqft")]')
                sqft = sqft_element.find_element(By.XPATH, './preceding-sibling::span').text
            except NoSuchElementException:
                sqft = "N/A"  # Set a default value if sqft is not found
                        
            # Create a unique filename based on the URL and order of processing
            filename = f"{batch_index + 1}_{url_index + 1}"  # Adding 1 for human-readable numbering
            output_csv_filename = os.path.join(desktop_path, f"{filename}_continued_about.csv")  # Save to the desktop directory
            
            # Save extracted data along with URL to a CSV file with the unique filename
            with open(output_csv_filename, "w", newline="", encoding="utf-8") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["URL", "Description", "Monthly Rent", "Beds", "Baths", "Sqft"])
                csv_writer.writerow([url, about_property_text, monthly_rent, beds, baths, sqft])
            
            print(f"CSV file saved for URL {url}")
        except Exception as e:
            urls_not_processed.append(url)  # Add the URL to the list of URLs not processed
            print(f"An error occurred for URL {url}: {e}")
    
    # Print URLs that weren't processed in this batch
    print(f"URLs not processed in batch {batch_index + 1}: {urls_not_processed}")
    
    # Switch to a different WiFi network after processing each batch
    if batch_index < len(url_batches) - 1:
        input("Switch to a different WiFi network. Press Enter to continue...")

# Close the web driver instances
driver.quit()