from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import methods

# setting up the driver and accessing the game
options = Options()
driver = webdriver.Chrome(options=options)
url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
# selecting english
eng_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, paths.lang_eng)))
eng_button.click()
# giving the game time to restart after selecting the language
time.sleep(1)
# allowing cookies
cookie_okay = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, paths.cookie_ok)))
cookie_okay.click()

# selecting the elements needed
big_cookie = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, paths.big_cookie)))
cookie_count = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, paths.number_of_cookies)))
# populating the lists that contain the prices and the shop items
shop_items = methods.store_items(driver)
store_prices = methods.store_prices(driver)

while 1:
    try:
        big_cookie.click()
    except:
        pass
    # transforming the cookie count into an int
    element_text = cookie_count.text.strip()
    cookie_count_stripped = element_text.split('\n')[0]
    cookie_count_split = element_text.split(' ')[0]
    cookie_count_int = methods.convert_to_numeric(cookie_count_split)
    # verifying if the something can be bought
    for i in range(0, len(store_prices)):
        if store_prices[i] < cookie_count_int:
            # buying and updating the list
            shop_items[i].click()
            store_prices = methods.store_prices(driver)
