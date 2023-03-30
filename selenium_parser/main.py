from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
browser = webdriver.Chrome()


url = 'https://hyundai-astana.kz/ru/find-a-car/'
browser.get(url)
# time.sleep(2)
# button = browser.find_element(By.CLASS_NAME,'popup-btn-close')
# button.click()

cars = browser.find_elements(By.CLASS_NAME,'carItem')
file = open('result.csv','w',encoding='utf-8',newline='')
writer = csv.writer(file)
writer.writerow(['Модель','Цена','ссылка'])
for car in cars:
    link = car.get_attribute('href')

    carname = car.find_element(By.CLASS_NAME,'carName').text
    carprice = car.find_element(By.CLASS_NAME,'carPrice').text
    if carname and carprice:

        print('Модель:',carname,'Цена:',carprice,'ссылка:',link)
        writer.writerow([carname,carprice,link])

file.close()


