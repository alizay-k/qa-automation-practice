from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Alizaayk/Desktop/qa_framework/test/login.html")
time.sleep(6)
driver.find_element(By.ID,"username").send_keys("Alizay")
driver.find_element(By.ID,"password").send_keys("falanadhimkana")
driver.find_element(By.ID,"loginBtn").click()

driver.find_element(By.ID,"message")

print(driver.title)
time.sleep(5)
driver.quit()

