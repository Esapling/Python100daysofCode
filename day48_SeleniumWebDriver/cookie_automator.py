"""
    this code is designed for creating a bot player for Cookie Clicker game 
    see for details "http://orteil.dashnet.org/experiments/cookie/"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


        
class CookieBot:
    def __init__(self):
        self.logger = logging.getLogger("CookieBot")
        logging.basicConfig(level=logging.INFO)
        logging.info("Class instantiated")
        self.driver = None

    def start(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
        self.setup_elements()
        self.play_game()

    def setup_elements(self):
        self.cookie_btn = self.driver.find_element(By.CSS_SELECTOR, "div#cookie")
        self.store = self.driver.find_elements(By.CSS_SELECTOR, 'div#store div')
        self.item_list = self.create_list()

    def create_list(self):
        item_list = []
        for item in self.store:
            info = item.find_element(By.TAG_NAME, "b").text
            if len(info) == 0:
                continue
            dict_ = {
                "name": info.split(" - ")[0],
                "money": int(info.split(" - ")[1].replace(',', '')), # the actual number represented using comma(,)
                "id": item.get_attribute('id')
            }
            item_list.append(dict_)
        return item_list

    def check_state(self):
        #checks the availabilty of purchasing some features from the store such as Cursor, Grandma , Factory, etc
        total_money = int(self.driver.find_element(By.CSS_SELECTOR, "div#money").text)
        for item in self.item_list[::-1]: 
            while total_money > item['money']: # from bottom to top continue buying the mostpowerful one if  we have enough money
                self.logger.info(f"Available product found {item['name']} to buy {total_money} - {item['money']} = {total_money-item['money']}")
                total_money -= item['money']
                self.driver.find_element(By.ID, item['id']).click()
                #storing selenium objects in a list to click them again is not helpful
                # after the first click it gives a DOM error
                #so for every click we need to relocate the clickable object 
                # item_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, item['id'])))
                # item_element.click()
                self.logger.info(f"Item {item['name']} is purchased, total budget {total_money}")
                
                
    def cookie_for_five_sec(self):
        #keeps cliclking the cookie button for 7 seconds
        start_time = time.time()
        while time.time() - start_time < 7:
            self.cookie_btn.click()

    def play_game(self):  
        while True:
            self.cookie_for_five_sec()
            self.check_state()          

    def promptCommentToScreen(self):
        print(self.driver.find_element(By.ID, value="comment"))

    def print_items_in_store(self):
        print(self.item_list)

    def close_game(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    try:
        cookie_bot = CookieBot()
        cookie_bot.start()
    except Exception as error:
        cookie_bot.logger.error(str(error))
    finally:
        cookie_bot.close_game()


#cookie_bot.play_game(state=True)

