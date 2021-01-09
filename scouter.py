import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os 

WEBHOOK = "https://discord.com/api/webhooks/758151139383443478/XURX5jr3xmCPN6OPoTV2bGP-YLhD8K_c4roR1_KivVZZ8TnPfOuuQqQVyrJdxQP1DV2A"
PATH = "/app/.chromedriver/bin/chromedriver"
print(PATH)
RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3080LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"

class Scouter():
    def __init__(self, link):
        self.link = link
    def sendToDiscord(self, link):
        d = {
        "content": "<@&691835932835577856>\nBuy Now:\n" + link
    }
        requests.post(WEBHOOK, json=d)
    def scout(self):
        driver = webdriver.Chrome(PATH)
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

scouter = Scouter("https://www.bestbuy.com/site/hyperx-cloud-alpha-pro-wired-stereo-gaming-headset-for-pc-ps4-xbox-one-blackout-black/6434292.p?skuId=6434292")
scouter.scout()

