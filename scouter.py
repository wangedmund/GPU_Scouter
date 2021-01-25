import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
from multiprocessing import Process
from webdriver_manager.chrome import ChromeDriverManager
import time

WEBHOOK = "https://discord.com/api/webhooks/758151139383443478/XURX5jr3xmCPN6OPoTV2bGP-YLhD8K_c4roR1_KivVZZ8TnPfOuuQqQVyrJdxQP1DV2A"
RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3070XPATH = '//button[@data-sku-id = "6429442"]'
RTX3080LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
RYZEN7LINK = "https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000"
RYZEN7XPATH = '//button[@data-sku-id = "6439000"]'

LOCAL_PATH = os.getcwd() + "\chromedriver.exe"

class Scouter():
    def __init__(self, link, name, XPATH):
        self.link = link
        self.name = name
        self.XPATH = XPATH
    def sendToDiscord(self, link):
        d = {
        "content": "<@&691835932835577856>\nBuy Now:\n" + link
        }
        requests.post(WEBHOOK, json=d)
    def scout(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
        # driver = webdriver.Chrome(LOCAL_PATH)
        driver.get(self.link)
        while True:
            try:
                elem = driver.find_element(By.XPATH, self.XPATH)
            except:
                print(self.name + " element could not be found!")
                driver.refresh()
                continue
            if (elem.text != 'Sold Out'):
                print(self.name + "'s " +  elem.text + " button found!")
                self.sendToDiscord(self.link)
                time.sleep(300)
            else:
                print(self.name + " sold out!")
            driver.refresh()
            
if __name__=='__main__':
    scouter1 = Scouter(RTX3070LINK, "3070", RTX3070XPATH)
    scouter2 = Scouter(RYZEN7LINK, "5800x", RYZEN7XPATH)
    p1 = Process(target = scouter1.scout)
    p1.start()
    p2 = Process(target = scouter2.scout)
    p2.start()
  
    
    


