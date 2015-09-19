# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest

class memberList_add(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_memberList_add(self):
        u"""会员管理新增会员测试"""
        addLog("会员管理新增会员测试")        
        driver=self.driver
        #打开服务管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"会员管理",u"会员列表")
        
        #获取当前记录数
        driver.switch_to_frame("main")
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"初始数目："+linetext
        n=linetext.find(u"。",0)
        line1=linetext[9:n-2]
        print line1
    
        #点击新增按钮,新增信息
        driver.find_element_by_id("sample_editable_1_new").click()
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("userAccount").send_keys("huiyuan")
        time.sleep(1)
        driver.find_element_by_id("userName").send_keys(u"新增会员")
        time.sleep(1)
        driver.find_element_by_id("userPwd").send_keys("123456")
        time.sleep(1)        
        driver.find_element_by_id("userMobile").send_keys("15269856456")
        time.sleep(1)
        driver.find_element_by_id("userEmail").send_keys("15269856456@163.com")
        time.sleep(1)        
        driver.find_element_by_id("useHospital").send_keys(u"济南市中心医院")
        time.sleep(1)
        driver.find_element_by_css_selector("#chk_share").click()       
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)
    
        #获取新增后的记录数，判断是否新增成功
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"新增后数目："+linetext
        n=linetext.find(u"。",0)
        line2=linetext[9:n-2]        
        print line2
        if int(line2)==int(line1)+1:
            print u"新增成功"
            addLog("会员管理新增会员测试成功")
        else:
            raise NameError(u"会员管理新增会员测试失败！")        

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()