# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest

class memberList_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_memberList_edit(self):
        u"""会员管理编辑会员测试"""
        addLog("会员管理编辑会员测试")        
        driver=self.driver
        #打开会员管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"会员管理",u"会员列表")
        
        #打开编辑页面
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        try:
            row=findInPage().findRow(driver,xpath,"huiyuan5",1)
            row.click()
        except AttributeError,msg:
            print u"编辑会员失败："+msg.message
            addLog("会员管理编辑会员测试失败：没有找到要编辑的会员")
            return
        #打开编辑页面
        editCell=findInPage().findCell(row,7)
        editCell.click()        
        #点击编辑按钮,编辑信息
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(u"新增会员修改")
        time.sleep(1)
        driver.find_element_by_id("userMobile").clear()
        driver.find_element_by_id("userMobile").send_keys("15269856451")
        time.sleep(1)
        driver.find_element_by_id("userEmail").clear()
        driver.find_element_by_id("userEmail").send_keys("15269856451@163.com")
        time.sleep(1)  
        driver.find_element_by_id("useHospital").send_keys(u"平阴县医院")   
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)
        
        #判断修改是否成功
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        row=findInPage().findRow(driver,xpath,"huiyuan5",1)
        newusername=findInPage().findCellTextInRow(row,1)
        newmobile=findInPage().findCellTextInRow(row,4)
        if newusername==u"新增会员修改" and newmobile=="15269856451":
            addLog("会员管理编辑会员测试成功")
        else:
            addLog("会员管理编辑会员测试失败")
            
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()