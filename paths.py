# language pop-up
lang_eng = "//div[@id='langSelect-EN']"
cookie_ok = "//a[contains(text(), 'Got')]"

# in-game
big_cookie = "//button[@id='bigCookie']"
number_of_cookies = "//div[@id='cookies']"
shop = "//div[@id='products']"
price = "//span[@class='price']"
shop_item = "//div[@id='product']"


def get_shop_item(product_number):
    return f"//div[@id='product{product_number}']"


def get_product_price(product_number):
    return f"//span[@id='productPrice{product_number}']"
