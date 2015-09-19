# -*- coding: utf-8 -*-

import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time
from types import *

class roleList_del(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()        
        
    def test_roleList_del(self):
        u"""删除角色测试"""
        addLog("删除角色测试")
        #打开角色管理页面
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
        
        #选中要删除的行
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        table=getTable()
        try:
            #row=table.getRow(driver,xpath,u"测试角色修改",1)
            row=findInPage().findRow(driver,xpath,u"测试角色修改",2)
            row.click()
        except AttributeError,msg:
            print u"删除角色失败："+msg.message
            addLog("角色删除测试失败，没有找到要删除的行")
            return
        #删除得到的行
        driver.find_element_by_id("btnDelete").click()
        time.sleep(2)
        #在弹出的确认删除对话框中点击是
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"是":
                btn.click()
        time.sleep(5)
        #点击删除成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()

        #判断删除测试是否成功
        #row=table.getRow(driver,xpath,u"测试角色修改",1)
        row=findInPage().findRow(driver,xpath,u"测试角色修改",2)
        if type(row)==NoneType:
            addLog("删除角色测试成功")
        else:
            addLog("删除角色测试失败")
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()