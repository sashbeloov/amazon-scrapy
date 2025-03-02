from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
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
url = 'https://www.amazon.in/s?k=laptop'




while True:
    laptop_links = []
    for i in range(3):
        driver.get(url)
    try:
        next_page = driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        print(f"next_page_url {next_page}")
        url = next_page.get_attribute('href')
    except:
        print('This is the last page!')
        break


    laptop_url = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    for url in laptop_url:
        l_links = url.get_attribute('href')
        laptop_links.append(l_links)

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
            ram = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-ram_memory.installed_size']"
                                                        "//span[@class='a-size-base po-break-word']").text
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
            cpu = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-cpu_model.family']"
                                                        "//span[@class='a-size-base po-break-word']").text
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
                                              "//tr[@class='a-spacing-small po-graphics_description']"
                                              "/td[2]/span").get_attribute("innerText").strip()
        except:
            description = 'No description'

        print(f'laptop_graphics_card_description:{description}')
        print("\n")
        laptop_graphics_card_description.append(description)

        count += 1

        # try:
        #     description = driver.find_element(By.XPATH,
        #                                       "//tr[@class='a-spacing-small po-graphics_description']"
        #                                       "//td//span[@class='a-size-base a-text-bold' and contains(text(), 'Graphics Card Description')]"
        #                                       "/parent::td/following-sibling::td/span").text.strip()
        # except:
        #     description = 'No description'

# df = pd.DataFrame(
#     {
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
#
#     }
# )
# df.to_csv('laptops.csv')
# df = pd.DataFrame(
#     {

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# book_titles = []
# book_authors = []
# book_prices = []
# book_ratings = []
# book_pages = []
# book_languages = []
# book_publishers = []
# reading_ages = []
# feedback_summaries = []
#
# count = 0  # Nechta kitob yig'ildi
# max_books = 50  # Maksimal kitob soni
# next_page_url = 'https://www.amazon.in/s?k=books'
#
# while count < max_books:  # Faqat 50 ta kitob yig'ilgunga qadar ishlaydi
#     book_links = []
#
#     driver.get(next_page_url)
#
#     # Keyingi sahifani topish
#     try:
#         next_page = driver.find_element(By.XPATH, "//a[contains(@class, 's-pagination-next')]")
#         next_page_url = next_page.get_attribute('href')
#     except:
#         print('This is the last page!')
#         break
#
#     # Kitoblarning URL larini olish
#     book_urls = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
#     for url in book_urls:
#         if count >= max_books:  # Agar 50 ta yig'ilsa, loopdan chiqish
#             break
#         book_links.append(url.get_attribute('href'))
#
#     # Har bir kitob uchun ma'lumot olish
#     for link in book_links:
#         if count >= max_books:  # 50 ta bo'lsa, loopdan chiqamiz
#             break
#         driver.get(link)
#
#         try:
#             title = driver.find_element(By.XPATH, "//span[@id='productTitle']").text
#         except:
#             title = 'No title'
#         book_titles.append(title)
#
#         try:
#             author = driver.find_element(By.XPATH, "//span[@class='author notFaded']//a").text
#         except:
#             author = 'No author'
#         book_authors.append(author)
#
#         try:
#             price = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))).text
#             price = float(price.replace(',', ''))
#         except:
#             price = 'No price'
#         book_prices.append(price)
#
#         try:
#             rating = driver.find_element(By.XPATH, "//span[@id='acrPopover']").get_attribute('title')
#             book_ratings.append(float(rating.split(' ')[0]))
#         except:
#             book_ratings.append(0.0)  # Agar rating topilmasa, 0 qo'yamiz
#
#         try:
#             page = driver.find_element(By.XPATH, "//span[contains(text(), 'pages')]").text
#             book_pages.append(int(page.split(' ')[0]))
#         except:
#             book_pages.append(0)  # Agar page topilmasa, 0 qo'yamiz
#
#         try:
#             language = driver.find_element(By.XPATH, "//div[@id='rpi-attribute-language']//span").text
#         except:
#             language = 'No language'
#         book_languages.append(language)
#
#         try:
#             publisher = driver.find_element(By.XPATH, "//div[@id='rpi-attribute-book_details-publisher']//span").text
#         except:
#             publisher = 'No publisher'
#         book_publishers.append(publisher)
#
#         try:
#             age = driver.find_element(By.XPATH, "//span[contains(text(), 'Reading age')]/following-sibling::span").text
#             age = int(age.split(' ')[0])
#         except:
#             age = 0  # Agar yosh topilmasa, 0 qo'yamiz
#         reading_ages.append(age)
#
#         try:
#             feedback = driver.find_element(By.XPATH, "//div[@id='product-summary']//p").text
#         except:
#             feedback = 'No feedback summary'
#         feedback_summaries.append(feedback)
#
#         count += 1  # Yig'ilgan kitoblar sonini oshiramiz
#
# # Ma'lumotlarni CSV faylga saqlash
# df = pd.DataFrame({
#     'title': book_titles,
#     'author': book_authors,
#     'price': book_prices,
#     'rating': book_ratings,
#     'language': book_languages,
#     'publisher': book_publishers,
#     'age': reading_ages,
#     'page': book_pages,
#     'feedback_summary': feedback_summaries
# })
#
# df.to_csv('books_az.csv', index=False)
# print("✅ 50 ta kitob yig'ildi va 'books_az.csv' saqlandi!")
