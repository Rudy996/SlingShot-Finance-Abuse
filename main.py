import re
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
options.add_extension("2Captcha.crx")


acc = 5
o = ("1")
mail42 = o * acc
api = ("")




def work(mail43):
    try:
        r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        mail = r.text
        mal = mail.replace('[', '').replace(']', '').replace('"', '')
        check = mal.split("@")
        c = ("bheps.com")
        h = ("dcctb.com")
        t = 0
        while t == 0:
            if check[1] == c:
                t = 1
            elif check[1] == h:
                t = 1
            else:
                r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
                mail = r.text
                mal = mail.replace('[', '').replace(']', '').replace('"', '')
                check = mal.split("@")
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="apiKey"]'))).send_keys(api)
        driver.find_element_by_id("autoSubmitForms").click()
        driver.find_element_by_id("autoSolveRecaptchaV2").click()
        driver.find_element_by_id("autoSolveRecaptchaV3").click()
        driver.find_element_by_id("connect").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        driver.get("https://slingshot.finance/mobile/RMC861ZSRUHC") # Реф.ссылка
        wait.until(EC.element_to_be_clickable((By.ID, 'top-input'))).send_keys(Keys.CONTROL + "a")
        wait.until(EC.element_to_be_clickable((By.ID, 'top-input'))).send_keys(Keys.DELETE)
        wait.until(EC.element_to_be_clickable((By.ID, 'top-input'))).send_keys(mal)
        wait.until(EC.element_to_be_clickable((By.ID, 'top-button'))).click()

        time.sleep(5)
        l = 0
        while l == 0:
            try:
                driver.find_element_by_class_name("layout_error__PsJG2")
                r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
                mail = r.text
                mal = mail.replace('[', '').replace(']', '').replace('"', '')
                wait.until(EC.element_to_be_clickable((By.ID, 'top-input'))).send_keys(Keys.CONTROL + "a")
                wait.until(EC.element_to_be_clickable((By.ID, 'top-input'))).send_keys(Keys.DELETE)
                time.sleep(0.5)
                wait.until(EC.element_to_be_clickable((By.ID, 'top-input'))).send_keys(mal)
                wait.until(EC.element_to_be_clickable((By.ID, 'top-button'))).click()
                time.sleep(0.5)
                l = 0
            except:
                l = 1
        id = 0
        while id == 0:
            try:
                mails = mal.split("@")

                h = requests.get(
                    f"https://www.1secmail.com/api/v1/?action=getMessages&login={mails[0]}&domain={mails[1]}")  # проверка письма
                y = h.json()[0]["id"]

                o = requests.get(
                    f'https://www.1secmail.com/api/v1/?action=readMessage&login={mails[0]}&domain={mails[1]}&id={y}')
                t = o.json()["body"]

                myString_list = [r.group("url") for r in (re.search("(?P<url>https?://[^\s]+)", i) for i in t.split(" ")) if
                                 r is not None]
                confirm1 = myString_list[5]
                confirm = confirm1.replace('"', '')
                driver.get(confirm)
                id = y
                time.sleep(5)
                try:
                    but = driver.find_elements_by_class_name("gUgZQ")
                    wait.until(EC.element_to_be_clickable((but[0]))).click()
                except:
                    print("")

            except:
                id = 0








    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=1)
    p.map(work, mail42)
