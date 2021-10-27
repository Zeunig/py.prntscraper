from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random
import secrets
import time
import os
# Neccessary things
path = "D:\chromedriver.exe"
driver = webdriver.Chrome(path)
print("Opening up the browser")
driver.get("https://prnt.sc/")
print("Preparing cookies...")
driver.find_element_by_css_selector('.css-47sehv').click()
time.sleep(2)
while True:
    rastgele = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
    site = str(f'http://prnt.sc/{rastgele}')
    time.sleep(1)
    print("Accessing this site: "+ site)
    driver.get(site)
    time.sleep(0.5)
    print("Downloading file...")
    time.sleep(2)
    filename = 'result'+''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))+'.png'
    x = driver.find_element_by_xpath('//*[@id="screenshot-image"]')
    print(x)
    with open(filename, 'wb') as file:
        file.write(driver.find_element_by_xpath('//*[@id="screenshot-image"]').screenshot_as_png)
        print("File successfully downloaded! File name : " + filename)