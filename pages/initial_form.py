from dataclasses import dataclass
from typing import Dict
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@dataclass
class FormElement:
    element_type: str  # Either "input" or "select"
    value: str  # Value to fill in the field


# Temp default data
temp_form_data = {
    1: FormElement(element_type="input", value=""),
    2: FormElement(element_type="select", value=""),
    3: FormElement(element_type="input", value=""),
    4: FormElement(element_type="input", value=""),
    5: FormElement(element_type="input", value=""),
    6: FormElement(element_type="input", value=""),
    7: FormElement(element_type="input", value=""),
    8: FormElement(element_type="input", value=""),
    9: FormElement(element_type="select", value="Eviction"),
}


def fill_page(driver: WebDriver, form_data: Dict[int, FormElement]) -> None:
    """Locate and fill the fields for the current page."""
    main_content_div: WebElement = driver.find_element(By.CLASS_NAME, "mainContentDiv")
    table_cells: list[WebElement] = main_content_div.find_elements(
        By.XPATH,
        ".//div//td[contains(@class, 'caseSearchFieldInput') and (.//input or .//select)]",
    )

    for index, cell in enumerate(table_cells, start=0):
        if index not in form_data:
            print(f"Skipping field {index} (not in form_data for this page)")
            continue

        try:
            element: WebElement = cell.find_element(By.XPATH, ".//input | .//select")
            form_entry: FormElement = form_data[index]

            print(
                f"Filling field {index} ({form_entry.element_type}) with value: {form_entry.value}"
            )

            if form_entry.element_type == "input":
                element.send_keys(form_entry.value)
            elif form_entry.element_type == "select":
                select = Select(element)
                select.select_by_visible_text(form_entry.value)
        except NoSuchElementException:
            print(f"Element not found for field {index}")
        except Exception as e:
            print(f"Error filling field {index}: {e}")


def submit_form(driver: WebDriver) -> None:
    """Submit the form by clicking the 'Begin Search' button."""
    try:
        begin_search_button: WebElement = driver.find_element(
            By.XPATH, "//input[@value='Begin Search']"
        )
        begin_search_button.click()
        print("Clicked 'Begin Search' button.")
    except NoSuchElementException:
        print("Begin Search button not found.")
