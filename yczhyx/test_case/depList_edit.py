# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time
from types import *

class depList_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()  
        
    def test_depList_edit(self):
        u"""部门管理编辑部门测试"""
        addLog("部门管理编辑部门测试")
        driver=self.driver
        #打开部门管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"权限管理",u"部门管理")
        
        #打开编辑页面
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        try:
            row=findInPage().findRow(driver,xpath,u"新增部门",2)
            row.click()
        except AttributeError,msg:
            print u"编辑部门失败："+msg.message
            addLog("部门管理编辑部门测试失败：没有找到要编辑的部门")
            return
        #打开编辑页面
        driver.find_element_by_id("btnEdit").click()
        driver.switch_to_default_content()
        time.sleep(1)
        driver.switch_to_frame("main")
        driver.find_element_by_id("departmentid").clear()
        driver.find_element_by_id("departmentid").send_keys("dep002")
        time.sleep(1)
        driver.find_element_by_id("departmentname").clear()
        driver.find_element_by_id("departmentname").send_keys(u"新增部门修改")
        time.sleep(1)
        driver.find_element_by_id("departmentDescription").clear()
        driver.find_element_by_id("departmentDescription").send_keys(u"新增部门描述修改")
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)        
            
        #判断修改是否成功
        row=findInPage().findRow(driver,xpath,u"新增部门修改",2)
        if type(row)==NoneType:
            addLog("部门管理编辑部门测试失败,没有找到修改后的信息")
        else:
            addLog("部门管理编辑部门测试成功")
            
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()