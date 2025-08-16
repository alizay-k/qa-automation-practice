from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

urls=["file:///C:/Users/Alizaayk/Desktop/qa-automation-practice/login_form.html","https://www.python.org","https://www.selenium.dev"]
driver=webdriver.Chrome()
driver.get(urls[0])
WebDriverWait(driver,10).until(lambda d: d.title!="")
for url in urls:
    driver.execute_script(f"window.open('{url}');")
    WebDriverWait(driver,10).until(lambda d: d.title!="")
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver,10).until(lambda d: d.title!="")
    if url.startswith("file:///"):
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"username")))
        driver.find_element(By.ID,"username").send_keys("alizay")
        driver.find_element(By.ID,"password").send_keys("khan")
        driver.find_element(By.ID,"loginBtn").click()

driver.quit()
    