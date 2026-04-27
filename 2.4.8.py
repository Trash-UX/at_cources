from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import math
import time
site = 'http://suninjuly.github.io/explicit_wait2.html'
sleep_time_short = 0
sleep_time_long = 10

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(site)

time.sleep(sleep_time_short)

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))


time.sleep(sleep_time_short)

book = browser.find_element(By.ID, 'book')
book.click()


x = browser.find_element(By.ID, "input_value")
calculated_result = str(math.log(abs(12*math.sin(int(x.text)))))

answer = browser.find_element(By.ID, "answer")
answer.send_keys(calculated_result)

submit = browser.find_element(By.ID, 'solve')
submit.click()

time.sleep(sleep_time_long)
