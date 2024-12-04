from dotenv import load_dotenv
import json

from scraper import get_products
from mail import send_email

load_dotenv()


def parse_products(products):
    with open("data.json", "r") as read_file:
        existing_drops = []
        content = read_file.read()
        if content:
            content = json.loads(content)
            if not content:
                return

            existing_drops = content["hotwheels"]

        new_drops = [
            item for item in products if item not in existing_drops]

        if len(new_drops):
            send_email(new_drops)

        return new_drops


def save_products(products, new_drops):
    if not len(products):
        return

    with open("data.json", "w") as file:
        json.dump({"hotwheels": products}, file, indent=2)
        print(len(new_drops), "car/s added!")


def main():
    products = get_products()
    new_drops = parse_products(products)
    save_products(products, new_drops)


main()
