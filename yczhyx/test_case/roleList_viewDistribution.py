# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time

class roleList_viewDistribution(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_roleList_viewDistribution(self):
        u"""角色管理查看权限测试"""
        addLog("角色管理查看权限测试")
        driver=self.driver
        #打开角色管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"权限管理",u"角色管理")
        #选中要查看权限的记录   
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        table=getTable()
        try:
            #row=table.getRow(driver, xpath, u"测试角色",1)
            row=findInPage().findRow(driver,xpath,u"测试角色",2)
            row.click()
        except AttributeError,msg:
            print u"查看权限失败："+msg.message
            addLog("角色管理查看权限测试失败，没有找到要查看权限的角色")
            return         
        driver.find_element_by_id("btnViewDistribution").click()
        
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        
        if driver.find_element_by_id("roleName").text==u"角色:测试角色":
            addLog("角色管理查看权限测试成功")
        else:
            addLog("角色管理查看权限测试失败")
            
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()