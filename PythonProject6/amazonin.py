from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


laptop_brand = []
laptop_model = []
laptop_screensize = []
laptop_ram = []
laptop_storage = []
laptop_cpumodel = []
laptop_operating_system = []
laptop_price = []
laptop_rating = []
laptop_review_count = []
laptop_graphics_card_description = []

count = 1

max_count = 100
next_page_url = "https://www.amazon.in/s?k=laptop"

while count <= max_count:
    laptop_links = []
    for i in range(3):
        driver.get(next_page_url)
    try:
        next_page = driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        print(next_page)
        next_page_url = next_page.get_attribute("href")
    except:
        print("end page")
        break

    laptop_url = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    for url in laptop_url:
        l_link = url.get_attribute("href")
        laptop_links.append(l_link)
    for link in laptop_links:
        driver.get(link)
    try:
        laptopbrand = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-brand']"
                                                    "//td[@class='a-span9']").text
    except:
        laptopbrand = "no laptopbrand"
    print(count)
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)

    try:
        laptopmodel = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-model_name']"
                                                    "//span[@class='a-size-base po-break-word']").text
    except:
        laptopmodel = "no laptopmodel"
    print(f"laptopmodel: {laptopmodel}")
    laptop_model.append(laptopmodel)

    try:
        screensize = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-display.size']"
                                                   "//span[@class='a-size-base po-break-word']").text
    except:
        screensize = "no screensize"
    print(f"screensize: {screensize}")
    laptop_screensize.append(screensize)

    try:
        laptop_ramm = driver.find_element(By.XPATH, "////th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Maximum Memory Supported')]"
                                                    "/following-sibling").text
    except:
        laptop_ramm = "no laptop_ramm"
    print(f"laptop_ramm: {laptop_ramm}")
    laptop_ram.append(laptop_ramm)

    try:
        storage = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']"
                                                "").text
    except:
        storage = "no storage"
    print(f"storage: {storage}")
    laptop_storage.append(storage)

    try:
        laptopbrand = driver.find_element(By.XPATH, "").text
    except:
        laptopbrand = "no laptopbrand"
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)

    try:
        laptopbrand = driver.find_element(By.XPATH, "").text
    except:
        laptopbrand = "no laptopbrand"
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)

    try:
        laptopbrand = driver.find_element(By.XPATH, "").text
    except:
        laptopbrand = "no laptopbrand"
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)

    try:
        laptopbrand = driver.find_element(By.XPATH, "").text
    except:
        laptopbrand = "no laptopbrand"
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)

    try:
        laptopbrand = driver.find_element(By.XPATH, "").text
    except:
        laptopbrand = "no laptopbrand"
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)

    try:
        laptopbrand = driver.find_element(By.XPATH, "").text
    except:
        laptopbrand = "no laptopbrand"
    print(f"laptopbrand: {laptopbrand}")
    laptop_brand.append(laptopbrand)
