#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime as date
import time


# In[19]:


opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver=webdriver.Chrome(executable_path="ENTER PATH OF CHROMIUM DRIVER HERE",options=opt)
driver.get("https://gmail.com")
driver.implicitly_wait(15)


# In[ ]:


def login(email,password):


# In[9]:


def turn_off_camera_and_mic():    
    driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div').click()
    driver.implicitly_wait(3000)
    #turn off mic
    driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div').click()
    driver.implicitly_wait(3000)
    time.sleep(4)
    driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
    driver.implicitly_wait(3000)


# In[ ]:


def getinput():
    email=input("Please enter your email (This email will be used to join meeting)")
    password=input("Enter password")
    return email,password


# In[7]:


def joinMeeting(meetingUrl):
    driver.get(meetingUrl)
    return meetingUrl


# In[ ]:





# In[8]:


def leaveMeeting():
    passBT=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[9]/div[2]/div[2]/div/div[1]')
    passBT.click()


# In[21]:


url=""
loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys("WRITE YOUR EMAIL HERE B/W THESE TWO QUOTES")
nextBT=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
nextBT.click()
time.sleep(2)
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("WRITE YOUR PASSWORD HERE BETWEEN THESE TWO QUOTES")
time.sleep(2)

passBT=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
passBT.click()
time.sleep(10)
while(1):
    meetingTime=pd.read_csv("google_meet_data.csv")
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    day=date.today().strftime("%A")
    for index,row in meetingTime.iterrows():
        if str(row['Start Time'])==current_time and str(row['Day'])==day:
            url=joinMeeting(row['url'])
            time.sleep(5)
            turn_off_camera_and_mic()
            time.sleep(70)

            
        if str(row['End Time'])==current_time and str(row['Day'])==day and str(row['url'])==url:
            leaveMeeting()
            url=""


# In[20]:





# In[ ]:




