from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#getting browser
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Alizaayk/Desktop/qa_framework/test/form.html")
wait = WebDriverWait(driver, 20)

# Fill text inputs
driver.find_element(By.ID,"fname").send_keys("alizay")
driver.find_element(By.ID,"lname").send_keys("Khan")

#Select radio button
driver.find_element(By.ID,"female").click()


# Check the checkbox
driver.find_element(By.ID,"subscribe").click()

# Select from dropdown
from selenium.webdriver.support.ui import Select
country_select = Select(driver.find_element(By.ID, "country"))
country_select.select_by_value("us")

# Click submit
driver.find_element(By.ID, "submitBtn").click()

time.sleep(2)
print(driver.title)
driver.quit()


