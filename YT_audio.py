from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class music():
    def __init__(self):
    
       self.driver=webdriver.Chrome(options=options)
       self .driver.implicitly_wait(10)

    def get_info(self,query):
        self.query=query   

       
        self.driver.get("https://www.youtube.com/")
        try:
           #By.NAME, 'search_query'
           video=self.driver.find_element(By.NAME, 'search_query')
           video.click()
           video.send_keys(query)
           video.send_keys(Keys.RETURN)
        except Exception as e:
            print(f'an error occured:{e}')
         

            enter = self.driver.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer[2]')
            enter.click()
        
            #print('some issuue')
        #video.send_keys('selenium')
           

#assist=music()
#assist.get_info("beliver")

