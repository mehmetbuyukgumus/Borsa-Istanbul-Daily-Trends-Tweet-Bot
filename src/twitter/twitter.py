from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime
import os
from dotenv import load_dotenv
import sys
sys.path.append("../borsa")
from data_scrapping.datas import name_increasing, name_decreasing, highest_price, least_price

date = datetime.now()
date_now = date.date()
load_dotenv(dotenv_path= "infos.env")
my_username = os.getenv("myUsername")
my_password = os.getenv("myPassword")

def connetion_to_account():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get("https://twitter.com/?lang=tr")
    time.sleep(1)
    browser.delete_all_cookies()
    time.sleep(1)
    time.sleep(2)
    # selecet_cookies = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/span/span")
    time.sleep(1)
    # selecet_cookies.click()
    time.sleep(1)
    sign_in_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
    sign_in_button.click()
    time.sleep(2)
    username = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    time.sleep(1)
    username.click()
    time.sleep(1)
    username.send_keys(my_username)
    time.sleep(2)
    next_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
    next_button.click()
    time.sleep(2)
    password_input = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    password_input.click()
    time.sleep(2)
    password_input.send_keys(my_password)
    log_in_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
    log_in_button.click()
    time.sleep(2)
    # browser.maximize_window()
    return browser

def tweeting_increasing(browser):
    tweet_limit = len(name_increasing)
    counter = 0
    while counter < tweet_limit:
        for i1, i2 in zip(name_increasing, highest_price):
            el = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
            ActionChains(browser).move_to_element(el).click(el).send_keys(f"{date_now} BİST'TE GÜNÜN ŞAMPİYONLARI!!! 🏅 #{i1} %{i2} artış oranıyla günün yükselenleri arasında yerini aldı 🚀⚡️💥📈").perform()
            time.sleep(2)
            send_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span")
            time.sleep(1)
            send_button.click()
            time.sleep(2)
            counter += 1
            
def tweeting_decrasing(browser):
    tweet_limit = len(name_decreasing)
    counter = 0
    while counter < tweet_limit:
        for i1, i2 in zip(name_decreasing, least_price):
            el = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
            ActionChains(browser).move_to_element(el).click(el).send_keys(f"{date_now} Günü düşüşle kapatanlar 👎🏻 #{i1} %{i2} düşüş oranıyla günün düşenleri arasında yerini aldı ⬇️🆘📉").perform()
            time.sleep(2)
            send_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span")
            time.sleep(1)
            send_button.click()
            time.sleep(2)
            counter += 1
