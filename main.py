from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_fear_and_greed_index():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://www.cnn.com/markets/fear-and-greed")
        time.sleep(5)  # Wait for JS to load content

        index_element = driver.find_element(By.CLASS_NAME, "market-fng-gauge__dial-number")
        print(f"Fear and Greed Index: {index_element.text.strip()}")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_fear_and_greed_index()
