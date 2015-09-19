# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest
from types import *
from selenium.webdriver.common.by import By

class informationList_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_informationList_edit(self):
        u"""资讯管理编辑资讯测试"""
        addLog("资讯管理编辑资讯测试")        
        driver=self.driver
        #打开资讯管理页面
        login().login(driver)
        openMenu().openMenu(driver,u"网站管理",u"资讯管理")
    
        #选中要编辑的行
        driver.switch_to_frame("main")
        by_table=By.XPATH
        by_page=By.XPATH
        value_table=".//*[@id='maingridgrid']/div[4]/div[2]"  
        value_page=".//*[@id='maingrid']/div[6]/div/div[8]/div[1]/span"
        try:
            row=findInPage().findRowBy(driver,by_table,value_table,by_page,value_page,u"新增资讯",1)
            row.click()
        except AttributeError,msg:
            print u"编辑失败："+msg.message
            addLog("资讯管理编辑资讯测试失败：没有找到要编辑的资讯")
            return
        #点击编辑按钮,编辑信息
        driver.find_element_by_css_selector("div.l-icon.l-icon-modify").click()
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("txtTitle").clear()
        driver.find_element_by_id("txtTitle").send_keys(u"新增资讯修改")
        time.sleep(1)
        driver.find_element_by_id("Summary").clear()
        driver.find_element_by_id("Summary").send_keys(u"新增资讯简介修改")
        time.sleep(1)
        driver.switch_to_frame("ueditor_0")
        #driver.find_element_by_css_selector("html.view body.view").click()
        driver.find_element_by_css_selector("html.view body.view").send_keys(u"新增资讯内容修改")
        time.sleep(1)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)       

        #判断是否修改成功
        row=findInPage().findRowBy(driver,by_table,value_table,by_page,value_page,u"新增资讯修改",1)
        if type(row)==NoneType:
            addLog("资讯管理编辑资讯测试失败，没有找到编辑后的信息")
        else:
            addLog("资讯管理编辑资讯测试成功")
            
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()