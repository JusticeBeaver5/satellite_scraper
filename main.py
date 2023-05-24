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
    for i in range(4, 208):
        name = tbody.find_elements(By.XPATH, '//tr')[0].find_elements(By.XPATH, f'/html/body/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[{i}]/td[1]')[0].text
        id = tbody.find_elements(By.XPATH, '//tr')[0].find_elements(By.XPATH, f'/html/body/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[{i}]/td[2]')[0].text
        write_to_csv(f'{name},{id}')
        # print(f'{name},{id}')
    driver.quit()



if __name__=='__main__':
    main()


