import requests
from bs4 import BeautifulSoup

# The URL and headers remain the same
URL = 'https://www.amazon.com/SAMSUNG-Technology-Intelligent-Turbowrite-MZ-V9S1T0B/dp/B0DHLFWBQ1/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Use a more stable CSS selector and handle potential errors
try:
    # This selector targets the element with class 'a-offscreen', often used for the main price
    price_element = soup.select_one('span.a-price span.a-offscreen')

    # Check if the element was found before trying to get its text
    if price_element:
        price = price_element.get_text().strip()
        print(f"The price is: {price}")
    else:
        print("Could not find the price. The page structure may have changed or the request was blocked.")

except Exception as e:
    print(f"An error occurred: {e}")