import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def wake_streamlit():
    print("Setting up headless Chrome browser...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # Replace with your exact app URL
    url = "https://noshaynavigations.streamlit.app/"
    print(f"Navigating to {url}...")
    
    try:
        driver.get(url)
        # Wait 15 seconds to give the JavaScript time to load and register activity
        time.sleep(15)
        print("Page loaded successfully. Streamlit app should be awake!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    wake_streamlit()

