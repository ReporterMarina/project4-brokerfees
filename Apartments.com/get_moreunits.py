from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Create a WebDriver instance
driver = webdriver.Chrome()

# Load the URL
url = "https://www.apartments.com/106-hyde-park-ave-boston-ma/jtz4jy7/"
driver.get(url)

# Find and click the "Unit Details" button
unit_details_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Unit Details')]")
unit_details_button.click()

# Wait for the information to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='unit-info']")))

# Extract the information
unit_info = driver.find_element(By.XPATH, "//div[@class='unit-info']").text
print(unit_info)

# Close the browser
driver.quit()

