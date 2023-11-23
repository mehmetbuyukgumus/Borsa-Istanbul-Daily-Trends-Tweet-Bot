import requests
from bs4 import BeautifulSoup

name_increasing = []
name_decreasing = []
highest_price = []
least_price = []
url1 = "https://uzmanpara.milliyet.com.tr/borsa/en-cok-artanlar/"
url2 = "https://uzmanpara.milliyet.com.tr/borsa/en-cok-azalanlar/?seans=gun"

def connection_increasing(url):    
    headers = {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"
        }
    page = requests.get(url, headers= headers)
    soup = BeautifulSoup(page.content, "lxml")
    return soup

def connection_decreasing(url):    
    headers = {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"
        }
    page = requests.get(url, headers= headers)
    soup = BeautifulSoup(page.content, "lxml")
    return soup

def get_name_increasing(soup):
    titles = soup.find_all("td", attrs = {"class" : "currency currency-up"})
    for title in titles:
        a_title = title.get_text()
        name_increasing.append(a_title)
def get_name_decreasing(soup):
    titles = soup.find_all("td", attrs = {"class" : "currency currency-down"})
    for title in titles:
        a_title = title.get_text()
        name_decreasing.append(a_title)
def ratio_increasing(soup):
    ratios = soup.find_all("td", attrs = {"class" : "degisim up"})
    for ratio in ratios:
        a_ratio = ratio.get_text()
        highest_price.append(a_ratio)
def ratio_decrasing(soup):
    ratios = soup.find_all("td", attrs = {"class" : "degisim down"})
    for ratio in ratios:
        a_ratio = ratio.get_text()
        least_price.append(a_ratio)