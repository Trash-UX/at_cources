from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser = webdriver.Chrome()
sleep_time_short = 1
sleep_time_long = 10
site = 'https://suninjuly.github.io/redirect_accept.html'


time.sleep(sleep_time_short)

browser.get(site)
butt_on = browser.find_element(By.CLASS_NAME, "trollface")

butt_on.click()

handle = browser.window_handles[1]
browser.switch_to.window(handle)

time.sleep(sleep_time_short)

input = browser.find_element(By.ID, "input_value")

math = str(math.log(abs(12*math.sin(int(input.text)))))

answer = browser.find_element(By.ID, "answer")

answer.send_keys(math)

finish = browser.find_element(By.CLASS_NAME, "btn-primary")

finish.click()

time.sleep(sleep_time_long)
