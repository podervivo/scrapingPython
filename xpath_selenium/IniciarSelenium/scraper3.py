import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By   

#iniciar url
driver= webdriver.Chrome()
url= "http://google.com/"
driver.maximize_window()
driver.get(url)
time.sleep(3)
