import selenium as selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
link ="https://docs.google.com/forms/d/e/1FAIpQLSdq75K7SINQqaGOV0K6ebC8n6XZ4wrAYYrqq3BUVBpPtrOyIA/viewform?usp=sf_link"
class FillForm:
    def __init__(self, service_install):
        self.driver= webdriver.Chrome(service=service_install)

    def fill_form(self, address, price, address_link):
        self.driver.maximize_window()
        self.driver.get(link)
        address_textbox= self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        time.sleep(2)
        address_textbox.send_keys(address)
        time.sleep(2)
        price_textbox= self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        time.sleep(2)
        price_textbox.send_keys(price)
        time.sleep(2)
        address_link_textbox= self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        time.sleep(2)
        address_link_textbox.send_keys(address_link)
        submit= self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        time.sleep(2)
        submit.click()
        time.sleep(5)
        submit_another_response= self.driver.find_element(By.LINK_TEXT,"Submit another response")
        submit_another_response.click()
        time.sleep(5)




