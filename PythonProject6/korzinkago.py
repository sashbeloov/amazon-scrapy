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