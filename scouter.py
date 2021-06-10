import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import threading
import sys
from webdriver_manager.chrome import ChromeDriverManager
import time

WEBHOOK = "https://discord.com/api/webhooks/758151139383443478/XURX5jr3xmCPN6OPoTV2bGP-YLhD8K_c4roR1_KivVZZ8TnPfOuuQqQVyrJdxQP1DV2A"
UWUWEBHOOK = "https://discord.com/api/webhooks/803854081953103892/1KUvD1y7EJkoD2VUXr4TX5GxuOYLJMGkfeXWjK0lOgBlinlohxHP7Z1YlHbsHS_Cm1Et"

RTX3060TILINK_NVIDIA = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402"
RTX3060TIXPATH_NVIDIA = '//button[@data-sku-id = "6439402"]'

RTX3060TILINK_GIGABYTE = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-eagle-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442485.p?skuId=6442485"
RTX3060TIXPATH_GIGABYTE = '//button[@data-sku-id = "6442485"]'

RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3070XPATH = '//button[@data-sku-id = "6429442"]'

RTX3070TILINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789"
RTX3070TIXPATH = '//button[@data-sku-id = "6465789"]'

RTX3080LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
RTX3080XPATH = '//button[@data-sku-id = "6429440"]'

RYZEN7LINK = "https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000"
RYZEN7XPATH = '//button[@data-sku-id = "6439000"]'

LOCAL_PATH = os.getcwd() + "\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--example-flag")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver3 = webdriver.Chrome(ChromeDriverManager().install())
class Scouter():
    def __init__(self, link, name, XPATH, driver):
        self.link = link
        self.name = name
        self.XPATH = XPATH
        
        self.driver = driver

    def sendToDiscord(self, link):
        d = {
        "content": "<@&691835932835577856>\nBuy Now:\n" + link
        }
        requests.post(UWUWEBHOOK, json=d)

    def scout(self):
        self.driver.get(self.link)
        while True:
            sys.stdout.flush()
            try:
                elem = self.driver.find_element(By.XPATH, self.XPATH)
            except:
                print(self.name + " element could not be found!")
                self.driver.refresh()
                continue
            if (elem.text != 'Sold Out' and elem.text != 'Coming Soon'):
                print(self.name + "'s " +  elem.text + " button found!")
                for i in range(3):
                    os.system('say "Graphics card potentially found"')
            else:
                print(self.name + " " + elem.text)
            self.driver.refresh()
            
if __name__=='__main__':
    scouter1 = Scouter(RTX3070LINK, "nvidia 3070", RTX3070XPATH, driver)
    p1 = threading.Thread(target = scouter1.scout).start()
    scouter2 = Scouter(RTX3080LINK, "nvidia 3080", RTX3080XPATH, driver2)
    p2 = threading.Thread(target = scouter2.scout).start()
    scouter3 = Scouter(RTX3070TILINK, "nvidia 3070ti", RTX3070TIXPATH, driver3)
    p3 = threading.Thread(target = scouter3.scout).start()
   
  
    
    


