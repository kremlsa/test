from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element_by_id("book")
button.click()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))	
treasure = browser.find_element_by_id("input_value")
x = treasure.text
y = calc(x)
input1 = browser.find_element_by_css_selector("[id=answer]")
input1.send_keys(y)
button = browser.find_element_by_css_selector("[type=submit]")
button.click()
