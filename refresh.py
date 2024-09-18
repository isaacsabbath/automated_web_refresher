import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# Initialize undetected ChromeDriver
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

# Open the target website
driver.get("https://www.youtube.com/")

# Function to perform random refresh
def random_refresh():
    while True:
        # Wait for a random interval between 30 to 60 seconds
        time.sleep(random.randint(30, 60))
        
        # Refresh the page
        driver.refresh()
        
        # Perform some random actions to mimic human behavior
        try:
            elements = driver.find_elements(By.TAG_NAME, "a")
            if elements:
                random.choice(elements).click()
                time.sleep(random.randint(5, 15))
                driver.back()
        except Exception as e:
            print(f"Error during random actions: {e}")

# Start the random refresh process
random_refresh()
