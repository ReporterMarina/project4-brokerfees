from bs4 import BeautifulSoup
import requests

# Create a list of example URLs
urls = [
    "https://www.apartments.com/1-blackstone-st-cambridge-ma-unit-1b/p9rpc5t/",
    "https://www.apartments.com/1-briarfield-rd-milton-ma-unit-a/3fpg6pg/",
    "https://www.apartments.com/1-devonshire-st-boston-ma/1xps3w4/",
    "https://www.apartments.com/the-laneway-roxbury-crossing-ma/cqn66ff/"
]

# Create an empty list to store extracted text
extracted_text_list = []

for url in urls:
    try:
        print(f"Processing URL: {url}")

        # Send an HTTP request with a custom User-Agent header
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the desired data from the soup object
        about_data_element = soup.select_one("#profileContent h2:contains('About') + p")
        
        # Check if about_data_element exists before extracting text
        if about_data_element:
            about_data_text = about_data_element.get_text(strip=True)

            # Append extracted text to the list
            extracted_text_list.append(about_data_text)
            print(f"Extracted Text: {about_data_text}")
        else:
            print("About data not found.")
    except Exception as e:
        print(f"An error occurred for URL {url}: {e}")

# You can now use the 'extracted_text_list' as needed
