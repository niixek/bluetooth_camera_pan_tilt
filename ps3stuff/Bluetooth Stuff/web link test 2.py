import webbrowser
from selenium import webdriver
import time
import urlllib
import urllib2

x = raw_input("Enter the URL")
refreshrate = 5
driver = webdriver.Chromium()
driver.get("http://" + x)
while True:
    time.sleep(refreshrate)
    driver.refresh()

