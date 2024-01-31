from selenium.webdriver.common.by import By
import paths
from decimal import Decimal


def store_items(driver):
    shop_items = []
    for i in range(0, 20):
        shop_item = driver.find_element(By.XPATH, paths.get_shop_item(i))
        shop_items.append(shop_item)
    return shop_items


def convert_to_numeric(value_str):
    # Define a mapping for words to numerical values
    word_to_number_mapping = {
        'octillion': Decimal('10') ** 27,
        'septillion': Decimal('10') ** 24,
        'sextillion': Decimal('10') ** 21,
        'quintillion': Decimal('10') ** 18,
        'quadrillion': Decimal('10') ** 15,
        'trillion': Decimal('10') ** 12,
        'billion': Decimal('10') ** 9,
        'million': Decimal('10') ** 6
    }

    # Remove commas and spaces from the string
    cleaned_str = value_str.replace(',', '').replace(' ', '')
    # Check if the value contains a word representation
    for word, numeric_value in word_to_number_mapping.items():
        if word in cleaned_str:
            # Extract the numeric part and multiply by the corresponding value
            numeric_part = cleaned_str.split(word)[0]
            numeric_part_cleaned = ''.join(char for char in numeric_part if char.isnumeric() or char == '.')
            numeric_part_cleaned = Decimal(numeric_part_cleaned)
            return int(numeric_part_cleaned * numeric_value)

    numeric_part_cleaned = ''.join(char for char in cleaned_str if char.isnumeric() or char == '.')
    # If no word representation is found, return the integer value
    return int(numeric_part_cleaned)


def store_prices(driver):
    shop_prices = []
    shop_prices_value = []
    for i in range(0, 20):
        shop_price_element = driver.find_element(By.XPATH, paths.get_product_price(i))
        shop_prices.append(shop_price_element)
        shop_price_str = shop_price_element.get_attribute('innerHTML')
        # converting store price
        shop_price_value = convert_to_numeric(shop_price_str)
        # appending store price to the store prices
        shop_prices_value.append(shop_price_value)
    return shop_prices_value
