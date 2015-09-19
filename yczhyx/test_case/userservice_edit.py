# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time
from types import *

class userservice_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()  
        
    def test_userservice_edit(self):
        u"""服务管理编辑服务测试"""
        addLog("服务管理编辑服务测试")
        driver=self.driver
        #打开服务管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"系统设置",u"服务管理")
        
        #打开编辑页面
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        try:
            row=findInPage().findRow(driver,xpath,u"新增服务",2)
            row.click()
        except AttributeError,msg:
            print u"编辑服务失败："+msg.message
            addLog("服务管理编辑服务测试失败：没有找到要编辑的服务")
            return
        #打开编辑页面
        editCell=findInPage().findCell(row,6)
        editCell.click()
        time.sleep(2)
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("userServiceName").clear()
        driver.find_element_by_id("userServiceName").send_keys(u"新增服务修改")
        time.sleep(1)
        driver.find_element_by_id("userServiceMoney").clear()
        driver.find_element_by_id("userServiceMoney").send_keys("100")
        time.sleep(1)
        driver.find_element_by_id("userServiceDescription").clear()
        driver.find_element_by_id("userServiceDescription").send_keys(u"新增服务描述修改")
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)        
            
        #判断修改是否成功
        row=findInPage().findRow(driver,xpath,u"新增服务修改",2)
        if type(row)==NoneType:
            addLog("服务管理编辑服务测试失败,没有找到修改后的信息")
        else:
            addLog("服务管理编辑服务测试成功")
            
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()