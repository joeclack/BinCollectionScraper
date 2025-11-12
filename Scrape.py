from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

s = Service("/usr/local/bin/chromedriver")

ChromeOptions = Options()
ChromeOptions.add_argument("headless")

driver = webdriver.Chrome(options=ChromeOptions)


def get_next_collection():
    driver.get("https://www.darlington.gov.uk/pwa-home/bins/")
    print("Waiting for webpage...")
    time.sleep(2)
    # decline_cookies_button = driver.find_element(By.XPATH, "//button[text()='I decline']")
    # print("Declining cookies...")
    # decline_cookies_button.click()
    # time.sleep(1)

    postcode_input_field = driver.find_element(By.ID, "Postcode")
    search_address_button = driver.find_element(By.ID, "js-find-your-address-button")

    postcode_input_field.send_keys("DL56RJ")
    search_address_button.click()

    print("Searching postcode...")
    time.sleep(1)

    address_dropdown = Select(driver.find_element(By.ID, "js-select-address"))
    address_dropdown.select_by_value("100110567936")  # 17, ST MICHAEL'S CRESCENT

    print("Getting results...")
    time.sleep(2)

    next_collection_element = driver.find_element(By.CLASS_NAME, "card-header-primary")
    next_collection_text = next_collection_element.text

    next_date_element = driver.find_element(By.CLASS_NAME, "collectionDate")
    next_date_text = next_date_element.text

    print("Next collection is " + next_collection_text + " " + next_date_text)


get_next_collection()
