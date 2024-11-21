from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def open_page(driver: WebDriver, url: str) -> None:
    """Open the given URL and handle the login dialog."""
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "LoginDialog"))
    )
    body_element = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(body_element).click().perform()
