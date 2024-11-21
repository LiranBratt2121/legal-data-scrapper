from msvcrt import getch
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.login_modal import open_page
from pages.initial_form import fill_page, submit_form, temp_form_data


def setup_driver() -> WebDriver:
    """Set up and return a WebDriver instance."""
    chrome_options = Options()
    return WebDriver(options=chrome_options)


if __name__ == "__main__":
    try:
        driver = setup_driver()
        open_page(driver, "https://core.duvalclerk.com/CoreCms.aspx?mode=PublicAccess")

        fill_page(driver, temp_form_data)
        submit_form(driver)
    except Exception as e:
        print(f"UnSupported expection happed (D:): {e}")
    finally:
        while getch().decode('utf-8').lower() != 'q':
            continue   
        print("q was pressed. Closing progrm") 
        driver.quit()