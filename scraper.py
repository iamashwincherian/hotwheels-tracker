from bs4 import BeautifulSoup
import requests

from config import URL


def get_products():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find("div", class_="product-show-right")
        new_product_list = []

        if products:
            hotwheel_items = products.find_all(
                "div", class_="show-product-small-bx")

            for item in hotwheel_items:
                name = item.find(
                    "div", class_="detail-text").find("h3").get_text().strip()
                new_product_list.append(name)

        return new_product_list
