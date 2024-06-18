import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, ElementClickInterceptedException


class CookieClickerBot:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 20)
        self.big_cookie = self.wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))

    def click_big_cookie(self):
        try:
            while True:
                try:
                    # Remove the overlay if it exists
                    self.driver.execute_script("document.getElementById('darken').style.display = 'none';")
                    self.big_cookie.click()
                except ElementClickInterceptedException:
                    print("ElementClickInterceptedException: Overlay is blocking the click")
                time.sleep(0.1)  # Small delay to prevent the loop from running too fast
        except NoSuchWindowException:
            print("NoSuchWindowException: The browser window was closed unexpectedly")
        finally:
            self.driver.quit()

    def buy_products(self):
        try:
            while True:
                try:
                    products = self.wait.until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product.unlocked.enabled")))
                    max_priced_product = None
                    max_price = 0
                    for product in products:
                        try:
                            price_text = product.find_element(By.CSS_SELECTOR, "span.price").text
                            price = int(price_text.replace(',', ''))  # Convert price to an integer
                            if max_priced_product is None or price > max_price:
                                max_priced_product = product
                                max_price = price
                        except Exception as e:
                            print(f"Error parsing price for a product: {e}")

                    if max_priced_product:
                        max_priced_product.click()
                        print(f"Clicked on product with price: {max_price}")
                except TimeoutException:
                    print("TimeoutException: The elements were not found within the given time")
                    print(self.driver.page_source)
                except Exception as e:
                    print(f"An error occurred during product processing: {e}")

                time.sleep(1)  # Delay to prevent the loop from running too fast
        except NoSuchWindowException:
            print("NoSuchWindowException: The browser window was closed unexpectedly")
        finally:
            self.driver.quit()

    def start(self):
        # Start the threads for clicking and buying
        click_thread = threading.Thread(target=self.click_big_cookie)
        buy_thread = threading.Thread(target=self.buy_products)

        click_thread.start()
        buy_thread.start()

        # Join the threads to ensure they complete before the script exits
        click_thread.join()
        buy_thread.join()


# URL of the Cookie Clicker game
url = "https://orteil.dashnet.org/cookieclicker/"

if __name__ == "__main__":
    bot = CookieClickerBot(url)
    bot.start()
