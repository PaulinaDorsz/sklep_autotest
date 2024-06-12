from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\Projects\TestFiles\chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:

    driver.get("https://skleptest.pl/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Contact')]"))).click()

    name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "your-name")))
    name_input.send_keys("Imię Nazwisko")

    email_input = driver.find_element(By.NAME, "your-email")
    email_input.send_keys("przyklad@email.com")

    subject_input = driver.find_element(By.NAME, "your-subject")
    subject_input.send_keys("Temat wiadomości")

    message_input = driver.find_element(By.NAME, "your-message")
    message_input.send_keys("Treść wiadomości")

    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

finally:
    driver.quit()


