from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request


def makedirs(p):
    try:
        if not os.path.exists(p):
            os.makedirs(p)
    except OSError:
        print("Error: Creating directory. " + directory)


keyword = "검색할데이터"
dataName = "data"
makedirs("D:/data/{}".format("crawlingData"))
chromedriver = "D:/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
time.sleep(3)

print(keyword, "검색")
driver.get("https://www.google.co.kr/imghp?hl=ko")
Keyword = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
Keyword.send_keys(keyword)
driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

print(keyword + " 스크롤 중 .............")
elem = driver.find_element_by_tag_name("body")
for i in range(100):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

time.sleep(1)
try:
    driver.find_element_by_xpath(
        '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input'
    ).click()
    for i in range(100):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass
time.sleep(2)

links = []
images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
for item in images:
    if item.get_attribute("src") != None:
        links.append(item.get_attribute("src"))
        print(keyword + " 찾은 이미지 개수:", len(links))
        time.sleep(2)

for index, item in enumerate(links):
    url = item
    start = time.time()
    urllib.request.urlretrieve(
        url, "D:/data/{}/{}.jpg".format("crawlingData", dataName + str(index))
    )
    print(
        str(index + 1)
        + "/"
        + str(len(links))
        + " "
        + keyword
        + " 다운로드 중....... Download time : "
        + str(time.time() - start)[:5]
        + " 초"
    )
    print(keyword + " ---다운로드 완료---")

driver.close()
