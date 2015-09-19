# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time
from types import *

class roleList_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()
        
    def test_roleList_edit(self):
        u"""编辑角色测试"""
        addLog("编辑角色测试")
        driver=self.driver
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"权限管理",u"角色管理")
        #driver.get(self.url)
        #driver.find_element_by_id("userAccount").clear()
        #driver.find_element_by_id("userAccount").send_keys("admin")
        #driver.find_element_by_id("password").clear()
        #driver.find_element_by_id("password").send_keys("123456")
        #driver.find_element_by_xpath("//div[2]/form/div[4]/button").click()
        #time.sleep(2)        
        #titles=driver.find_elements_by_css_selector(".title")
        #for title in titles:
            #if title.text==u"权限管理":
                #title.click()
        #time.sleep(2)
        #driver.find_element_by_link_text(u"角色管理").click()
        #time.sleep(2) 
        
        #选中要编辑的行
        #参数xpath用户获取table控件        
        driver.switch_to_frame("main")        
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        try:
            #row=table.getRow(driver, xpath, u"测试角色",1)
            row=findInPage().findRow(driver,xpath,u"测试角色",2)
            row.click()
        except AttributeError,msg:
            print u"编辑角色失败："+msg.message
            addLog("编辑角色测试失败，没有找到要编辑的角色")
            return      
        #row=table.getRow(driver, xpath, u"测试角色11",1)
        #row.click()        
        #打开编辑页面
        driver.find_element_by_id("btnEdit").click()
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("rolename").clear()
        driver.find_element_by_id("rolename").send_keys(u"测试角色修改")
        driver.find_element_by_id("rolemark").clear()
        driver.find_element_by_id("rolemark").send_keys(u"测试角色描述修改") 
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.green").click()
        time.sleep(5)        

        #判断是否修改成功
        row=findInPage().findRow(driver, xpath, u"测试角色修改",2)
        if type(row)==NoneType:
            addLog("编辑角色测试失败，没有找到编辑后的信息")
        else:
            addLog("编辑角色测试成功")
        
        
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()