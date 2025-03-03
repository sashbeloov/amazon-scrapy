# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# laptop_brand = []
# laptop_model = []
# laptop_screensize = []
# laptop_ram = []
# laptop_storage = []
# laptop_cpumodel = []
# laptop_operating_system = []
# laptop_price = []
# laptop_rating = []
# laptop_review_count = []
# laptop_graphics_card_description = []
#
#
# count = 1
# next_page_url = 'https://www.amazon.in/s?k=laptop'
#
#
# while True:
#     laptop_links = []
#     for i in range(3):
#         driver.get(next_page_url)
#     try:
#         next_page = driver.find_element(By.XPATH,
#                                         "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
#         print(f"next_page_url {next_page}")
#         next_page_url = next_page.get_attribute('href')
#     except:
#         print('This is the last page!')
#         break
#
#     laptop_url = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
#     for url in laptop_url:
#         l_link = url.get_attribute('href')
#         laptop_links.append(l_link)
#     for link in laptop_links:
#         driver.get(link)
#         try:
#             laptopbrand = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-brand']"
#                                                         "//td[@class='a-span9']").text
#         except:
#             laptopbrand = 'No laptopbrand'
#         print(count)
#         print('laptop_brand: ', laptopbrand)
#         laptop_brand.append(laptopbrand)
#
#         try:
#             laptopmodel = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-model_name']"
#                                                         "//span[@class='a-size-base po-break-word']").text
#         except:
#             laptopmodel = 'No laptopmodel'
#         print('laptop_model: ', laptopmodel)
#         laptop_model.append(laptopmodel)
#
#         try:
#             screensize = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-display.size']"
#                                                         "//span[@class='a-size-base po-break-word']").text
#         except:
#             screensize = 'No screensize'
#         print('laptop_screensize: ', screensize)
#         laptop_screensize.append(screensize)
#
#         try:
#             ram = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-ram_memory.installed_size']"
#                                                         "//span[@class='a-size-base po-break-word']").text
#         except:
#             ram = 'No ram'
#         print('laptop_ram: ', ram)
#         laptop_ram.append(ram)
#
#         try:
#             storage = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']"
#                                                     "//span[@class='a-size-base po-break-word']").text
#         except:
#             storage = 'No storage'
#         print('laptop_storage: ', storage)
#         laptop_storage.append(storage)
#
#         try:
#             cpu = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']"
#                                                         "//span[@class='a-size-base po-break-word']").text
#         except:
#             cpu = 'No cpu'
#         print('laptop_cpumodel: ', cpu)
#         laptop_cpumodel.append(cpu)
#
#         try:
#             operating_system = driver.find_element(By.XPATH,
#                                                    "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Operating System')]"
#                                                    "/following-sibling::td").text
#         except:
#             operating_system = 'No operating_system'
#         print('Operating_system:', operating_system)
#         laptop_operating_system.append(operating_system)
#
#         try:
#             price = driver.find_element(By.XPATH,
#                                         "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
#                                         "//span"
#                                         "//span[@class='a-price-whole']").text
#         except:
#             price = 'No price'
#         print('laptop_price: ', price)
#         laptop_price.append(price)
#
#         try:
#                 rating = driver.find_element(By.XPATH, "//span[@class='reviewCountTextLinkedHistogram noUnderline']").text
#         except:
#             rating = 'No rating'
#         print('laptop_rating: ', rating)
#         laptop_rating.append(rating)
#
#         try:
#             review_count = driver.find_element(By.XPATH, "//span[@id='acrCustomerReviewText']").text
#         except:
#             review_count = 'No review_count'
#         print('review_count: ', review_count)
#         laptop_review_count.append(review_count)
#
#         try:
#             description_element = WebDriverWait(driver, 10).until(
#                 expected_conditions.visibility_of_element_located(
#                     (By.XPATH, "//tr[contains(@class, 'a-spacing-small po-graphics_description')]/td[2]/span")))
#             description = description_element.text
#         except:
#             description = 'No description'
#
#         print(f'laptop_graphics_card_description:{description}')
#         print("\n")
#         laptop_graphics_card_description.append(description)
#
#         count += 1
#
# df = (pd.DataFrame
#         ({
#         'laptop-brand': [laptop_brand],
#         'laptop-model': [laptop_model],
#         'laptop-screensize': [laptop_screensize],
#         'laptop-ram': [laptop_ram],
#         'laptop-storage': [laptop_storage],
#         'laptop-cpu': [laptop_cpumodel],
#         'laptop-operating_system': [laptop_operating_system],
#         'laptop-price': [laptop_price],
#         'laptop-rating': [laptop_rating],
#         'laptop-review_count': [laptop_review_count],
#         'laptop-graphics_card_description': [laptop_graphics_card_description],
#         }))
# df.to_csv('laptops.csv')
#
#
#
#         # try:
#         #     description = driver.find_element(By.XPATH,
#         #                                       "//tr[@class='a-spacing-small po-graphics_description']"
#         #                                       "/td[2]"
#         #                                       "/span[@class='a-size-base po-break-word']").text
#         # except:
#         #     description = 'No description'
#


# <<<<<--------------------------------------------------->>>>


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
next_page_url = 'https://www.amazon.in/s?k=laptop'
max_laptops = 100

while count <= 100:
    laptop_links = []
    for i in range(3):
        driver.get(next_page_url)
    try:
        next_page = driver.find_element(By.XPATH,
                                        "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        print(f"next_page_url {next_page}")
        next_page_url = next_page.get_attribute('href')
    except:
        print('This is the last page!')
        break

    laptop_url = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    for url in laptop_url:
        l_link = url.get_attribute('href')
        laptop_links.append(l_link)
    for link in laptop_links:
        driver.get(link)
        try:
            laptopbrand = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-brand']"
                                                        "//td[@class='a-span9']").text
        except:
            laptopbrand = 'No laptopbrand'
        print(count)
        print('laptop_brand: ', laptopbrand)
        laptop_brand.append(laptopbrand)

        try:
            laptopmodel = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-model_name']"
                                                        "//span[@class='a-size-base po-break-word']").text
        except:
            laptopmodel = 'No laptopmodel'
        print('laptop_model: ', laptopmodel)
        laptop_model.append(laptopmodel)

        try:
            screensize = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-display.size']"
                                                        "//span[@class='a-size-base po-break-word']").text
        except:
            screensize = 'No screensize'
        print('laptop_screensize: ', screensize)
        laptop_screensize.append(screensize)

        try:
            ram = driver.find_element(By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Maximum Memory Supported')]"
                                                   "/following-sibling::td").text
        except:
            ram = 'No ram'
        print('laptop_ram: ', ram)
        laptop_ram.append(ram)

        try:
            storage = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']"
                                                    "//span[@class='a-size-base po-break-word']").text
        except:
            storage = 'No storage'
        print('laptop_storage: ', storage)
        laptop_storage.append(storage)

        try:
            cpu = driver.find_element(By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Processor Type')]"
                                                   "/following-sibling::td").text
        except:
            cpu = 'No cpu'
        print('laptop_cpumodel: ', cpu)
        laptop_cpumodel.append(cpu)

        try:
            operating_system = driver.find_element(By.XPATH,
                                                   "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Operating System')]"
                                                   "/following-sibling::td").text
        except:
            operating_system = 'No operating_system'
        print('Operating_system:', operating_system)
        laptop_operating_system.append(operating_system)

        try:
            price = driver.find_element(By.XPATH,
                                        "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
                                        "//span"
                                        "//span[@class='a-price-whole']").text
        except:
            price = 'No price'
        print('laptop_price: ', price)
        laptop_price.append(price)

        try:
                rating = driver.find_element(By.XPATH, "//span[@class='reviewCountTextLinkedHistogram noUnderline']").text
        except:
            rating = 'No rating'
        print('laptop_rating: ', rating)
        laptop_rating.append(rating)

        try:
            review_count = driver.find_element(By.XPATH, "//span[@id='acrCustomerReviewText']").text
        except:
            review_count = 'No review_count'
        print('review_count: ', review_count)
        laptop_review_count.append(review_count)

        try:
            description = driver.find_element(By.XPATH,
                                                  "//td[@class='a-size-base prodDetAttrValue']").text
        except:
            description = 'No description'

        print(f'laptop_graphics_card_description:{description}')
        print("\n")
        laptop_graphics_card_description.append(description)

        count += 1

df = (pd.DataFrame
        ({
        'laptop-brand': [laptop_brand],
        'laptop-model': [laptop_model],
        'laptop-screensize': [laptop_screensize],
        'laptop-ram': [laptop_ram],
        'laptop-storage': [laptop_storage],
        'laptop-cpu': [laptop_cpumodel],
        'laptop-operating_system': [laptop_operating_system],
        'laptop-price': [laptop_price],
        'laptop-rating': [laptop_rating],
        'laptop-review_count': [laptop_review_count],
        'laptop-graphics_card_description': [laptop_graphics_card_description],
        }))
df.to_csv('laptops.csv')

