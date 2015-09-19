# -*- coding: utf-8 -*-
#本文档用户登录系统

from selenium import webdriver
import time,os,csv,unittest
import HTMLTestRunner

class login(object):
    def __init__(self):
        #self.url="http://192.168.1.252:8010/WebSystem/login.aspx"
        self.url="http://115.28.169.230:8010/websystem/login.aspx"
        pass

    def init(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()  
        return self.driver
    
    #param driver:webdriver的实例
    #param url：要登录的系统地址    
    def login(self,mydriver):
        driver=mydriver
        #登录系统
        driver.get(self.url)
        driver.find_element_by_id("userAccount").clear()
        driver.find_element_by_id("userAccount").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//div[2]/form/div[4]/button").click() 
        time.sleep(2)
        
    def __del__(self):
        pass

if __name__=="__main__":
    mylogin=login()
    driver=mylogin.init()
    url="http://192.168.1.252:8010/WebSystem/login.aspx"
    mylogin.login(driver)
    driver.quit()