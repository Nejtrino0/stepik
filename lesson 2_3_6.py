from selenium import webdriver
from math import *
import time


def calc(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    first_name = browser.find_element_by_css_selector('button.btn').click()

    first_window = browser.window_handles[0]

    w = browser.window_handles[1]

    browser.switch_to.window(w)

    file = browser.find_element_by_css_selector('span#input_value').text
    a = calc(int(file))

    a = browser.find_element_by_css_selector('input#answer').send_keys(str(a))

    n = browser.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(3)
finally:
    browser.quit()
