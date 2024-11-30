from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from utils import find_id, save_to_file


def move_page(driver: WebDriver) -> bool:
    button_XPATH = '//*[contains(@id, "c_NextPageButton")]'

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_XPATH))
        )

        button = driver.find_element(By.XPATH, button_XPATH)

        if button.get_attribute("disabled"):
            return False

        button.click()
        return True

    except StaleElementReferenceException:
        print("Element became stale. Trying again...")
        return move_page(driver)


def get_table_ids(driver: WebDriver):
    page_number = 1
    all_ids = set()

    while True:
        tbodies_XPATH = "//table[@class='searchResultsTable']//tbody"

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tbodies_XPATH))
        )

        try:
            tbodies = driver.find_elements(By.XPATH, tbodies_XPATH)
            ids = {find_id(tbody.get_attribute("onclick")) for tbody in tbodies}
            all_ids.update(ids)
        except StaleElementReferenceException:
            print("Stale element reference detected. Retrying...")
            continue 
            
        save_to_file(page_number, ids)
                
        if move_page(driver):
            page_number += 1
            continue

        return all_ids, page_number
