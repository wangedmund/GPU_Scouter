import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

WEBHOOK = "https://discord.com/api/webhooks/758151139383443478/XURX5jr3xmCPN6OPoTV2bGP-YLhD8K_c4roR1_KivVZZ8TnPfOuuQqQVyrJdxQP1DV2A"
PATH = "E:\Desktop\GPU_Scouter\chromedriver.exe"
RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
def sendToDiscord(item):
    d = {
        "content": "<@&691835932835577856>\nBuy Now:\n" + item
    }
    requests.post(WEBHOOK, json=d)
driver = webdriver.Chrome(PATH)


driver.get(RTX3070LINK)
while True:
    try:
        elem = driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
    except:
        print("element could not be found")
        driver.refresh()
        continue
    print("add to cart button open")
    sendToDiscord(RTX3070LINK)
    break

