from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\Projects\TestFiles\chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:
    driver.get("https://skleptest.pl/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Blog')]"))).click()

finally:
    driver.quit()
