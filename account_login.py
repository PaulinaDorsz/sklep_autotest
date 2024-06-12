from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicjalizacja serwisu ChromeDrivera
service = Service("C:\Projects\TestFiles\chromedriver.exe")

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(service=service)

try:
    # Otwarcie strony
    driver.get("https://skleptest.pl/")

    # Kliknięcie na "Account"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Account')]"))).click()

    # Wprowadzenie adresu e-mail
    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    email_input.send_keys("test@wp.pl")

    # Wprowadzenie hasła
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Testowehaslo")

    # Kliknięcie na "Login"
    submit_button = driver.find_element(By.XPATH, "//input[@type='login']")
    submit_button.click()

finally:
    # Zamknięcie przeglądarki
    driver.quit()


