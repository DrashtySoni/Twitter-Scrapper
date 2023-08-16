import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Define the list of usernames to scrape
usernames = ["bright_data"]

# Function to scrape user profile
def scrape_profile(username):
    URL = "https://twitter.com/" + username + "?lang=en"
    
    # Set up a new Selenium driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Load the URL in the Selenium driver
    driver.get(URL)
    
    # Wait for the webpage to be loaded
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
    except WebDriverException:
        print(f"Tweets for {username} did not appear! Proceeding after timeout")
        driver.quit()
        return
    
    # Extract and print the information (similar to your existing code)
    name = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserName"]').text.split('\n')[0]
    bio = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserDescription"]').text
    location = driver.find_element(By.CSS_SELECTOR,'span[data-testid="UserLocation"]').text
    website = driver.find_element(By.CSS_SELECTOR,'a[data-testid="UserUrl"]').text
    join_date = driver.find_element(By.CSS_SELECTOR,'span[data-testid="UserJoinDate"]').text
    following_count = driver.find_element(By.XPATH, "//span[contains(text(), 'Following')]/ancestor::a/span").text
    followers_count = driver.find_element(By.XPATH, "//span[contains(text(), 'Followers')]/ancestor::a/span").text
    tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

    # Print the collected information
    print("Name\t\t: " + name)
    print("Bio\t\t: " + bio)
    print("Location\t: " + location)
    print("Website\t\t: " + website)
    print("Joined on\t: " + join_date)
    print("Following count\t: " + following_count)
    print("Followers count\t: " + followers_count)


    # Close the Selenium driver
    driver.quit()

# Set maximum number of workers (parallel threads)
max_workers = 10  # You can adjust this based on your system's capacity

# Use concurrent.futures to scrape profiles in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(scrape_profile, usernames)

# Introduce a delay to manage overall scraping rate
time.sleep(180)  # 180 seconds for each set of usernames