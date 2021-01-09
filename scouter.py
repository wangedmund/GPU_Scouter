import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os 
import sys

WEBHOOK = "https://discord.com/api/webhooks/758151139383443478/XURX5jr3xmCPN6OPoTV2bGP-YLhD8K_c4roR1_KivVZZ8TnPfOuuQqQVyrJdxQP1DV2A"
RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3080LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"

LOCAL_PATH = os.getcwd() + "\chromedriver.exe"

class Scouter():
    def __init__(self, link):
        self.link = link
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
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        # driver = webdriver.Chrome(LOCAL_PATH)
        driver.get(self.link)
        while True:
            try:
                driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
            except:
                print("element could not be found")
                driver.refresh()
                continue
            print("add to cart button open")
            self.sendToDiscord(self.link)
            break
inp = sys.argv[1]
link = ""
if inp == "3070":
    link = "https://www.bestbuy.com/site/hyperx-cloud-alpha-pro-wired-stereo-gaming-headset-for-pc-ps4-xbox-one-blackout-black/6434292.p?skuId=6434292"
elif inp == "3080":
    link = "https://www.bestbuy.com/site/hyperx-cloud-alpha-wired-stereo-gaming-headset-for-pc-ps4-xbox-one-and-nintendo-switch-red-black/6100109.p?skuId=6100109"
else:
    raise KeyboardInterrupt
scouter = Scouter(link)
scouter.scout()


