from selenium import webdriver
import time
import urllib

x = input("Enter the URL: ")
refreshrate = 5
driver = webdriver.Chromium()
driver.get("http://" + x)
while True:
    time.sleep(refreshrate)
    driver.refresh()
