from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome('')
browser.get(start_url)
time.sleep(8)

def scrap():
    headers = [
    'Proper name',
    'Distance(ly)',
    'Mass (M☉)',
    'Radius (R☉)',
    ]
    planet_data = []
    for i in range(0,447):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for th_tag in soup.find_all("th",attrs={"class","exoplanet"}):
            tr_tags = th_tag.find_all("tr")
            temp_list = []
            for index,tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all()[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])  
                    except:
                        temp_list.append('')
            planet_data.append(temp_list)  
scrap()