import requests
from bs4 import BeautifulSoup


class PriceTracker:

    def __init__(self, url):
        self.url = url

    def get_title(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(self.url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        title = soup.find(id="productTitle")

        if title:
            return title.text.strip()

        return "Title not found"

    def get_price(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(self.url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        price = soup.select_one("span.a-price-whole")

        if price:
            return price.text.strip()

        return "Price not found"


url = "https://www.amazon.in/iPhone-16-Plus-256-GB/dp/B0DGJ8DP1M/"

product = PriceTracker(url)

print("Product Name :", product.get_title())
print("Product Price :", product.get_price())