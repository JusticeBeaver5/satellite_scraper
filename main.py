'''
This method is for parsing satellite ids from web page at n2yo.com.
Should not be used anymore since there is a better way of requesting it using API.
This code will be kept only for educational purpose on how to use selenium.
For requesting satellites use request_satellites.py

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv


url = 'https://www.n2yo.com/satellites/?c=JPN&t=country'
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)



def write_to_csv(data):
    with open('database.csv','a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', lineterminator = '\n')
        writer.writerows(data)


def main(url):
    driver.get(url)
    tbody = driver.find_element(By.XPATH, '/html/body/table[1]/tbody/tr/td[2]/table[2]/tbody')
    # print(tbody.find_elements(By.XPATH, '//tr')[1].text)
    write_to_csv([['name', 'sat_id']])
    for i in range(4, 204):
        name = tbody.find_elements(By.XPATH, '//tr')[0].find_elements(By.XPATH, f'/html/body/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[{i}]/td[1]')[0].text
        sat_id = tbody.find_elements(By.XPATH, '//tr')[0].find_elements(By.XPATH, f'/html/body/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[{i}]/td[2]')[0].text
        
        write_to_csv([[name,sat_id]])
        print(f'{name},{sat_id}')
    driver.quit()



if __name__=='__main__':
    main(url)



