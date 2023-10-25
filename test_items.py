from selenium.webdriver.common.by import By
import time


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_present(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-primary"))
    assert button > 0, 'Element is ot found'



