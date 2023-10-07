from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Before Using
# Make sure you have shortcuts set to ON on your fb acc :)


grupa_czy_osoba = input("what are u choosing?? (group-chat/person): ")

if grupa_czy_osoba == "person":
    imie = input("name of a person you want to troll: ")
    nazwisko = input("surname of a person you want to troll: ")
    osoba = imie + " " + nazwisko
else:
    osoba = input("the name of the group-chat: ")

email = input("your email: ")
hasło = input("your password")

wiadomosc = input("what message you want to spam: ")


driver.get("https://www.facebook.com")
time.sleep(1)
webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
time.sleep(1)
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys(email)
password.send_keys(hasło)
webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
time.sleep(5)
webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()
time.sleep(5)
webdriver.ActionChains(driver).send_keys("q").perform()
time.sleep(2)
webdriver.ActionChains(driver).send_keys(osoba).perform()
time.sleep(1)
webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
time.sleep(4)
if grupa_czy_osoba == "person":
    for i in range(6):
        webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
while True:
    webdriver.ActionChains(driver).send_keys(wiadomosc).perform()
    webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
    time.sleep(2)
