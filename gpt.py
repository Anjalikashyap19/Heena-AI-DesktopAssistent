from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Music:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)  # Implicit wait for all elements

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/")
        
        try:
            # Explicit wait until the search box is visible
            search_box = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="search-input"]'))
            )
            search_box.click()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"An error occurred: {e}")

assist = Music()
assist.get_info("dynamite by bts")
