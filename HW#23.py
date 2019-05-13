import os
import urllib.request

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://dou.ua/")

sponsors_block_xpath = "//div[@class='items table']//a/img"

sponsors_block = driver.find_elements_by_xpath(sponsors_block_xpath)

newpath = (os.getcwd() + '\\logo_img\\')

if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in sponsors_block:
    url = i.get_attribute("src")
    filename = (newpath + i.get_attribute("alt") + "_logo.png")
    urllib.request.urlretrieve(url, filename)

driver.close()
