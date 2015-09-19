# -*- coding: utf-8 -*-
#本文档用于在左侧树中打开某个菜单项页面
from selenium import webdriver
import time

class openMenu(object):
    def __init__(self):
        pass
    
    def initMenu(self):
        self.driver=webdriver.Chrome()
        url="http://192.168.1.252:8010/WebSystem/login.aspx"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_id("userAccount").clear()
        self.driver.find_element_by_id("userAccount").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//div[2]/form/div[4]/button").click()
        time.sleep(2)  
        return self.driver
        
    def openMenu(self,mydriver,titlename,linkname):
        driver=mydriver
        driver.implicitly_wait(10)
        titles=driver.find_elements_by_css_selector(".title")
        #print titlename
        for title in titles:
            print "title:"+title.text
            if title.text==titlename:
                title.click()
                break
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(linkname).click()
        time.sleep(2)         
    
    def __del__(self):
        pass
    
if __name__=="__main__": 
    
    #打开权限管理--角色管理
    page=openMenu()
    driver=page.initMenu()
    page.openMenu(driver,u"权限管理",u"角色管理")
    
    driver.quit()