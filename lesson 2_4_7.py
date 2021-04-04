from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import *

browser = webdriver.Chrome()


def calc(x):
    return log(abs(12 * sin(x)))


try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR,
            "h5#price"), "100")
    )

    book_button = browser.find_element(By.CSS_SELECTOR, "button#book").click()
    b = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    a = calc(int(b))
    c = browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(str(a))
    jj = browser.find_element(By.CSS_SELECTOR, "button#solve").click()

finally:
    browser.quit()
