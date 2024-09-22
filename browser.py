from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class infowl():
    def __init__(self):
    
       self.driver=webdriver.Chrome(options=options)

    def get_info(self,query):
        self.query=query   

       
        self.driver.get("https://www.google.co.in/")
        self .driver.implicitly_wait(60)
        search=self.driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        search.click()
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
       # enter =  self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
        #enter.click()
        #search.send_keys('selenium')

        #firstweb =self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3')
        #search.send_keys(Keys.RETURN)
        


#assist=infowl()
#assist.get_info("Artifitial intelligence")



