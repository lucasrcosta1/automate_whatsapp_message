import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

def greetings ():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        return "Good morning"
    elif 12 <= currentTime.hour < 18:
        return "Good afternoon"
    else:
        return "Good night"
   

browser = webdriver.Chrome()
table = pd.read_excel("send.xlsx")

for row in table.index:
    name      = table.loc[row, "name"]
    phone     = table.loc[row, "phone"]
    message   = (table.loc[row, "message"]).replace("{}",name)
    
    browser.get("https://web.whatsapp.com")

    #wait api load 
    while len(browser.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)  
        
    if phone != "N":
        link = "https://web.whatsapp.com/send?phone={}&text={}".format(phone,message)
        browser.get(link)
            
        while len(browser.find_elements(By.ID, 'side')) < 1:
            try:
                time.sleep(2)
                alert = browser.switch_to.alert
                alert.accept()
            except: time.sleep(1)
                
        time.sleep(2) # só uma garantia
        if len(browser.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
            # enviar a mensagem
            browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            try:
                time.sleep(2)
                alert = browser.switch_to.alert
                alert.accept()
            except: time.sleep(2)
