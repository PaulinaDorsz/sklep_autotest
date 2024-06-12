from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\Projects\TestFiles\chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:
    driver.get("https://skleptest.pl/")

    title = driver.title
    print("Tytuł strony:", title)

finally:
    driver.quit()



