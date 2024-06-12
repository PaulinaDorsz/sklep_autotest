from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\Projects\TestFiles\chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:
    driver.get("https://skleptest.pl/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Account')]"))).click()

    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "reg_email")))
    email_input.send_keys("test@wp.pl")

    password_input = driver.find_element(By.ID, "reg_password")
    password_input.send_keys("Testowehaslo")

    submit_button = driver.find_element(By.XPATH, "//input[@type='Register']")
    submit_button.click()

finally:
    driver.quit()
