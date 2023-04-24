from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

quill_email="eamaple@mail.com"
quill_password="example_pass"

# Headless Driver
def getDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("user-agent=Mozilla/5.0" + str(random.randint(1,9000)) + " (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--enable-features=NetworkService')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    return driver

def quill_login(driver):
    driver.maximize_window()
    driver.get("http://quillbot.com/login")
    sleep(3)
    while driver.execute_script("""return document.getElementsByClassName("MuiFilledInput-input")""") == []:
        pass
    driver.execute_script(f'document.querySelector("#mui-3").value="{quill_email}"')
    driver.execute_script(f'document.querySelector("#mui-4").value="{quill_password}"')
    driver.execute_script('document.querySelector(".MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.MuiButtonBase-root.auth-btn.css-v7do75").click()')

def get_quill_text(text):
    driver = getDriver()
    quill_login(driver)
    sleep(7)
    driver.find_element(By.XPATH,"//span[6]").click()  # Increase Synonyms score
    driver.find_element(By.XPATH, "//div[@id='paraphraser-input-box']").send_keys(text)  # Send text
    sleep(2)
    driver.find_element(By.XPATH, "//div[@class='css-1fz2g01']").click() # Rephrase Button
    sleep(6)
    Rephrase_data = driver.find_element(By.XPATH, "//div[@id='paraphraser-output-box']").text  # Get Rephrase
    driver.quit()
    return Rephrase_data

result = get_quill_text(""" Lorem Ipsum is simply dummy text of the printing and typesetting industry.""")

print(result)
