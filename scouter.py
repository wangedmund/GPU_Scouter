import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os 
from multiprocessing import Process

WEBHOOK = "https://discord.com/api/webhooks/758151139383443478/XURX5jr3xmCPN6OPoTV2bGP-YLhD8K_c4roR1_KivVZZ8TnPfOuuQqQVyrJdxQP1DV2A"
RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3080LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
RYZEN7LINK = "https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000"
HYPERXBLACK = "https://www.bestbuy.com/site/hyperx-cloud-alpha-pro-wired-stereo-gaming-headset-for-pc-ps4-xbox-one-blackout-black/6434292.p?skuId=6434292"
HYPERXRED = "https://www.bestbuy.com/site/hyperx-cloud-alpha-wired-stereo-gaming-headset-for-pc-ps4-xbox-one-and-nintendo-switch-red-black/6100109.p?skuId=6100109"

LOCAL_PATH = os.getcwd() + "\chromedriver.exe"

class Scouter():
    def __init__(self, link, name):
        self.link = link
        self.name = name
    def sendToDiscord(self, link):
        #<@&691835932835577856>
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
        driver = webdriver.Chrome(LOCAL_PATH)
        driver.get(self.link)
        while True:
            try:
                elem = driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
            except:
                print(self.name + " could not be found")
                driver.refresh()
                continue
            print(self.name + " add to cart button found")
            # self.sendToDiscord(self.link)
            
if __name__=='__main__':
    scouter1 = Scouter(RTX3070LINK, "3070")
    scouter2 = Scouter(RYZEN7LINK, "5800x")
    p1 = Process(target = scouter1.scout)
    p1.start()
    p2 = Process(target = scouter2.scout)
    p2.start()


