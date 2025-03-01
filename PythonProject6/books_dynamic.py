from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
book_titles = []
book_authors = []
book_prices = []
book_ratings = []
book_pages = []
book_languages = []
book_publishers = []
reading_ages = []
feedback_summaries = []

count = 1
next_page_url = 'https://www.amazon.in/s?k=books'


while True:
    book_links = []
    for i in range(3):
        driver.get(next_page_url)
    try:
        next_page = driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        print(f"next_page_url {next_page}")
        next_page_url = next_page.get_attribute('href')
    except:
        print('This is the last page!')
        break


#a-link-normal s-line-clamp-2 s-link-style a-text-normal

    book_urls = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    for url in book_urls:
        b_link = url.get_attribute('href')
        book_links.append(b_link)


    for link in book_links:
        driver.get(link)
        try:
            title = driver.find_element(By.XPATH, "//span[@id='productTitle']").text
        except:
            title = 'No title'
        print(count)
        print('Title', title)
        book_titles.append(title)

        try:
            author = driver.find_element(By.XPATH, "//span[@class='author notFaded']"
                                               "//a").text
        except:
            author = 'No author'
        print('Author', author)
        book_authors.append(author)

        try:
            # price = driver.find_element(By.XPATH, "//span[@class='a-price-whole']").text
            price = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))).text
            price = float(price)
            if price == '':
                price = driver.find_element(By.XPATH, "//span[@class='a-size-base a-color-price a-color-price']").text
                price = float(price.replace('₹', ''))


        except:
            price = 'No price'
        print(f'Price: {price}')
        book_prices.append(price)

        try:
            rating = driver.find_element(By.XPATH, "//span[@id='acrPopover']")
            rating = rating.get_attribute('title')
            book_ratings.append(float(rating.split(' ')[0]))  # Преобразуем только если найден рейтинг
        except:
            rating = 'No rating'
            book_ratings.append(0.0)  # Если рейтинга нет, добавляем 0.0

        print(f"Rating: {rating}")

        try:
            page = driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-none a-text-center rpi-attribute-value']"
                                                 "//span[contains(text(), 'pages')]").text
            if page == '':
                print('Page chqaromadi!')
                page = driver.find_element(By.XPATH, "//span[@class='a-list-item']"
                                                         "//span[@class='a-text-bold' and contains(text(), 'Paperback')]"
                                                         "/following-sibling::span").text
            book_pages.append(int(page.split(' ')[0]))
        except:
            page = 'No page'

        print(f"Page number: {page}")


        try:
            language = driver.find_element(By.XPATH, "//div[@id='rpi-attribute-language']"
                                                      "//div[@class='a-section a-spacing-none a-text-center rpi-attribute-value']"
                                                 "//span").text
            if language == '':
                print('Language chqaromadi!')
                language = driver.find_element(By.XPATH, "//span[@class='a-list-item']"
                                                          "//span[@class='a-text-bold' and contains(text(), 'Language')]"
                                                          "/following-sibling::span").text

        except:
            language = 'No language'
        book_languages.append(language)
        print(f"Language: {language}")

        try:
            publisher = driver.find_element(By.XPATH, "//div[@id='rpi-attribute-book_details-publisher']"
                                                      "//div[@class='a-section a-spacing-none a-text-center rpi-attribute-value']"
                                                 "//span").text
            if publisher == '':
                # print('Publisher chqaromadi!')
                publisher = driver.find_element(By.XPATH, "//span[@class='a-list-item']"
                                                          "//span[@class='a-text-bold' and contains(text(), 'Publisher')]"
                                                          "/following-sibling::span").text

        except:
            publisher = 'No publisher'
        book_publishers.append(publisher)
        print(f"Publisher: {publisher}")

        try:
            age = driver.find_element(By.XPATH, "//span[@class='a-list-item']"
                                                "//span[@class='a-text-bold' and contains(text(), 'Reading age')]"
                                                "/following-sibling::span").text


            if age == '':
                print('Age chqaromadi!')
                age = driver.find_element(By.XPATH, "//div[@id='rpi-attribute-book_details-customer_recommended_age']"
                                                    "//div[@class='a-section a-spacing-none a-text-center rpi-attribute-value']"
                                                    "//span").text
            age = age.split(' ')
            print(age)
            age = int(age[age.index('years') - 1])
            print(age)
            reading_ages.append(age)


        except:
            age = 'No reading age'
        print(f"Reading age: {age}")

        try:
            feedback = driver.find_element(By.XPATH, "//div[@id='product-summary']"
                                                      "//p[@class='a-spacing-small']"
                                                 "//span").text
        except:
            feedback = 'No feedback summary'
        feedback_summaries.append(feedback)
        print(f"Feedback summary: {feedback}")


        count += 1

df = pd.DataFrame(
    {
        'title': [book_titles],
        'author': [book_authors],
        'price': [book_prices],
        'rating': [book_ratings],
        'language': [book_languages],
        'publisher': [book_publishers],
        'age': [reading_ages],
        'page': [book_pages],
        'feedback_summary': [feedback_summaries]

    }
)
df.to_csv('books_az.csv')

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
# max_books = 100  # Maksimal kitob soni
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
# print("✅ 1000 ta kitob yig'ildi va 'books_az.csv' saqlandi!")
