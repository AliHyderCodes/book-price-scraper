# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 19:43:30 2025

@author: Uzair Ahmed
"""

# Web Scraper: Book Titles & Prices from books.toscrape.com
# Author: Ali Hyder
# Description: Scrapes all book titles and prices from the homepage of books.toscrape.com
# and saves the data to a CSV file.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = "http://books.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'  # Fix encoding issue with special characters

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all book containers
books = soup.find_all("article", class_="product_pod")

# Step 4: Extract title and price from each book
book_data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    book_data.append({"Title": title, "Price": price})

# Step 5: Convert to DataFrame and save as CSV
df = pd.DataFrame(book_data)
df.to_csv("books.csv", index=False)

print("✅ Scraping complete! Data saved to books.csv")
