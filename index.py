import requests
from webdriver_manager.chrome import ChromeDriverManager
import pymongo 
from selenium import webdriver
from bs4 import BeautifulSoup
import os

print(os.getcwd())
# set up web driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get('https://hargapangan.id/')
html = driver.page_source

#get page markup 
soup = BeautifulSoup(html, 'html.parser')

med_size_garlic = soup.select('a[commodityid="12"]')
print(med_size_garlic)



#submit_button = driver.find_elements_by_xpath('//*[@id="pricelist-99"]/h3/span/i[2]')[0]
#submit_button.click()




