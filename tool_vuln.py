# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome driver with the Service object
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# # Navigate to the Amazon search page for drills
# driver.get("https://www.amazon.com/s?k=drill&crid=1IG2VK9WT9MQR&sprefix=%2Caps%2C1773&ref=nb_sb_noss")

# # Wait for the price element to be visible on the page (max wait time 10 seconds)
# try:
#     price = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-base a-color-secondary']"))
#     )
#     print("Price: ", price.text)
# except Exception as e:
#     print("Error:", e)

# # Close the browser
# driver.quit()
# ==============================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in full screen
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
chrome_options.add_argument("--headless")  # Uncomment if you want to run without opening Chrome

# Install and launch ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Get the page to scrape
scrape = input("What page would you like to scrape? ")

try:
    # Open the target website
    driver.get(scrape)

    # Wait for the elements to load
    time.sleep(3)  # Adjust if necessary

    # Extract repository names (modify the selector based on the page structure)
    elements = driver.find_elements(By.CLASS_NAME, "repo")  # Adjust selector as needed
    links = [el.text for el in elements]

    # Print extracted data
    print("\nExtracted Data:")
    for link in links:
        print(link)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")

# Close the browser
driver.quit()
