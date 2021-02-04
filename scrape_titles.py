from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

base_url = "https://www.youtube.com/channel/UCTZUTvv_1Onm-f-533Hyurw/videos"

driver = webdriver.Firefox()
driver.get(base_url)
    

#Keep scrolling until dynamic content runs out
prev_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(1.5)
    current_height = driver.execute_script("return document.documentElement.scrollHeight")
    if current_height == prev_height:
        break
    prev_height = current_height
    
#Grab video titles from BeautifulSoup
soup = BeautifulSoup(driver.page_source,  "html.parser")
titles = soup.find_all("a", id="video-title", class_="ytd-grid-video-renderer" , title=True)

with open("titles.txt", "w") as f:
    f.write("\n".join(list(map(lambda x: x.text, titles))))
