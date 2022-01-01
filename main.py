from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser)

driver.get("https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800")
parent = driver.title
words = driver.find_elements(by=By.CSS_SELECTOR, value=".Kore a")
driver.execute_script("window.open('about:blank','secondtab');")
number = 1
for word in words:
    word = word.text

    driver.switch_to.window("secondtab")
    driver.get(f'https://www.google.com/search?q=korean+to+english+{word}')

    pronunciation = driver.find_element(by=By.CSS_SELECTOR, value="#tw-source-rmn-container span").text
    translation = driver.find_element(by=By.CSS_SELECTOR, value="#kAz1tf span.Y2IQFc").text

    print(number, word, pronunciation, translation)

    driver.switch_to.window(driver.window_handles[0])
    with open("learn-korean.txt", "a", encoding="utf-8-sig") as file:
        file.write(f"{number}  {word}  {pronunciation}  {translation}\n")

    number += 1
