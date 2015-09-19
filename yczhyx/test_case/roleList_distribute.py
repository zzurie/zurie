# -*- coding: utf-8 -*-
#角色管理中分配权限测试
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time
from types import *

class roleList_distribute(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()        
        
    def test_roleList_distribute(self):
        u"""角色管理分配权限测试"""
        addLog("角色管理分配权限测试")
        #打开角色管理页面
        driver=self.driver
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"权限管理",u"角色管理")
        
        #打开分配权限页面
        driver.switch_to_frame("main")
        #选中要分配权限的记录
        #参数xpath用户获取table控件               
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        table=getTable()
        try:
            #row=table.getRow(driver, xpath, u"测试角色",1)
            row=findInPage().findRow(driver,xpath,u"测试角色",2)
            row.click()
        except AttributeError,msg:
            print u"分配权限失败："+msg.message
            addLog("角色管理分配权限测试失败，没有找到要分配权限的角色")
            return          
        driver.find_element_by_id("btnDistribution").click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        #分配权限
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        #选择菜单项3权限管理，4角色管理，6网站管理，7设备管理
        checks[3].click()
        checks[4].click()
        checks[6].click()   
        checks[7].click()
        #保存选定的权限
        driver.find_element_by_id("btnEdit").click()
        time.sleep(10)
        
        #判断分配权限是否成功
        if driver.find_element_by_css_selector(".caption").text==u"角色列表":
            addLog("角色管理分配权限测试成功")
        else:
            addLog("角色管理分配权限测试失败")
            
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()