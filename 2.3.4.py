from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser = webdriver.Chrome()
sleep_time_short = 1
sleep_time_long = 10
site = 'http://suninjuly.github.io/alert_accept.html'


time.sleep(sleep_time_short)

browser.get(site)
butt_on = browser.find_element(By.CSS_SELECTOR, "button.btn")

butt_on.click()
time.sleep(sleep_time_short)
popup = browser.switch_to.alert
popup.accept()

input = browser.find_element(By.ID, "input_value")

math = str(math.log(abs(12*math.sin(int(input.text)))))

answer = browser.find_element(By.ID, "answer")

answer.send_keys(math)

finish = browser.find_element(By.CLASS_NAME, "btn-primary")

finish.click()

time.sleep(sleep_time_long)
