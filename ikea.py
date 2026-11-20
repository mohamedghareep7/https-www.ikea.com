from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
driver.maximize_window()

all_products = []

for pages in range(1,6):
    driver.get(f"https://www.ikea.com/eg/en/search/?q=ceiling-lights&page={pages}")
    print("page " , pages)
    time.sleep(2)

    container = driver.find_elements(By.XPATH , '//div[contains(@class , "plp-mastercard") and contains(@class , "plp-fragment-wrapper")]')
    for item in container:
        try:
            name = item.find_element(By.CLASS_NAME ,"plp-price-module__product-name").text
            print(name)
        except:
            name = 'no name found'
            print(name)

        try:
            description = item.find_element(By.CLASS_NAME, "plp-price-module__product-link").get_attribute("aria-label")
            print('description :' , description)
        except:
            description = "no description" 
            print('description :' , description)

        try:
            price = item.find_element(By.XPATH , './/span[@class="plp-price__sr-text"]').text
            price = price.replace('Price ' , '')
            print('price :' , price)
        except:
            price = 'no price found'
            print('price :' , price)

        available = item.find_element(By.XPATH , './/span[@class="plp-status__label"]').text
        print(available)

        product_image = item.find_element(By.XPATH , './/img[contains(@class , "plp-image")]').get_attribute('src')
        print('product_image :' , product_image)

        product_link = item.find_element(By.XPATH , './/a[contains(@class , "plp-product__image-link link")]').get_attribute("href")
        print('product_link :' , product_link)
        print("="*20)

        dic_products = {
            "name" : name,
            "description" : description,
            "price" : price,
            "available" : available,
            "product_image" : product_image,
            "product_link" : product_link
        }

        all_products.append(dic_products)

header = all_products[0].keys()
path = "all products.csv"


with open(path , "w" , encoding="utf-8" , newline="") as file :
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)


input("press Enter to close :")
driver.quit()

