from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import re
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
from datetime import date
from authentication import password

CONNECTION_STRING = "mongodb+srv://ryan:" + password + "@nilecluster1.8ujon.mongodb.net/PIHPSData?retryWrites=true&w=majority"

print(CONNECTION_STRING)

client = MongoClient(CONNECTION_STRING)
db = client.PIHPSData
dataCol = db.dailyData





browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://hargapangan.id/')
time.sleep(20)
html = browser.page_source

#get page markup 
soup = BeautifulSoup(html, 'html.parser')


page1_indicies = [
    ("Green Cayenne Pepper","15"),
    ("Red Cayenne Pepper","16"),
    ("Branded Cooking Oil Packaged 2","19"),
    ("Curly Red Chili","14"),
    ("Bulk Cooking Oil","17"),
    ("Super Quality Rice II", "6"),
    ("Beef Quality 1","8"),
    ("Beef Quality 2","9"),
    ("Fresh Chicken Eggs","10"),
    ("Branded Cooking Oil 1","18"),
    ("Premium Quality Sugar","20"),
    ("Local Sugar","21"),
]

page2_indicies = [
    ("Medium Size Shallots","11"),
    ("Big Red Chili","13"),
    ("Fresh Chicken Meat","7"),
    ("Medium Size Garlic","12"),
    ("Medium Size Garlic","12"),
    ("Low Quality Rice I","1"),
    ("Low Quality Rice II","2"),
    ("Medium Quality Rice I","3"),
    ("Medium Quality Rice II","4"),    
    ("Super Quality Rice I","5")
]  

page3_indicies = [
    ("Super Quality Rice II","6"),
    ("Beef Quality 1","8"),
    ("Beef Quality 2","9"),
    ("Fresh Chicken Eggs","10"),
    ("Branded Cooking Oil 1","18"),
]



dailyDataDict = {}

#get page 1
for commodity in page1_indicies:

    name = commodity[0]
    id = commodity[1]
    anchor = soup.find('a', {'commodityid': id})

    children = anchor.find_all("div", {'class': "price_now"})

    for child in children:
        text = child.get_text()
        new_text = re.findall("\d+\.\d+", text)
        final_text = new_text[0].replace('.',',')

        print(name)
        print(final_text)

        dailyDataDict[name] = final_text

#get page 2

submit_button = browser.find_elements_by_xpath('//*[@id="pricelist-99"]/h3/span/i[2]')[0]
submit_button.click()
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

for commodity in page2_indicies:

    name = commodity[0]
    id = commodity[1]
    anchor = soup.find('a', {'commodityid': id})

    children = anchor.find_all("div", {'class': "price_now"})

    for child in children:
        text = child.get_text()
        new_text = re.findall("\d+\.\d+", text)
        final_text = new_text[0].replace('.',',')

        print(name)
        print(final_text)

        dailyDataDict[name] = final_text

#get page 3

submit_button = browser.find_elements_by_xpath('//*[@id="pricelist-99"]/h3/span/i[2]')[0]
submit_button.click()
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

for commodity in page3_indicies:

    name = commodity[0]
    id = commodity[1]
    anchor = soup.find('a', {'commodityid': id})

    children = anchor.find_all("div", {'class': "price_now"})

    for child in children:
        text = child.get_text()
        new_text = re.findall("\d+\.\d+", text)
        final_text = new_text[0].replace('.',',')

        print(name)
        print(final_text)

        dailyDataDict[name] = final_text

browser.quit()


today = date.today().strftime("%m/%d/%Y")

data = {
    'date' : today,
    'data': dailyDataDict
}

print(data)

x = dataCol.insert_one(data)




