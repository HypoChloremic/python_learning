from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


#replace with your firefox profile

fp=webdriver.FirefoxProfile('C:\\Users\\Ali Rassolie\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\m\\n')

#enter your url here

url="https://pingpong.ki.se/courseId/5753/content.do?id=3860490"
driver = webdriver.Firefox(fp)
driver.get(url)

html_source = driver.page_source
print(html_source)