# -*- coding: utf-8 -*-

from selenium import webdriver
import time,os,csv

driver=webdriver.Firefox()
url = "http://192.168.1.252:8010/WebSystem/login.aspx"
with open("F:\learn\parameter.csv",'rb') as csvfile:
    parameter=csv.reader(csvfile,delimiter=',')
    for username,password in parameter:
        t=time.strftime("%Y%m%d-%H%M%S")
        print t
        print username,password
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_id("userAccount").send_keys(username)
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//div[2]/form/div[4]/button").click()
        driver.get_screenshot_as_file("/"+t+".png")

        #退出系统
        driver.find_element_by_xpath("//div[1]/div/div/div/div[3]/a").click()