# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest

class userList_add(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_userList_add(self):
        u"""员工管理新增员工测试"""
        addLog("员工管理新增员工测试")        
        driver=self.driver
        #打开员工管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"员工管理",u"员工列表")
        
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
        driver.find_element_by_id("userCode").send_keys("gonghao3")
        time.sleep(1)
        driver.find_element_by_id("userName").send_keys(u"新增员工")
        time.sleep(1)
        driver.find_element_by_id("userSex").send_keys(u"女")
        time.sleep(1)
        driver.find_element_by_id("useHospital").send_keys(u"济南市中心医院")
        time.sleep(1)
        driver.find_element_by_id("userAccount").send_keys("gonghao3")
        time.sleep(1)
        driver.find_element_by_id("userPwd").send_keys("123456")
        time.sleep(1)
        checks=driver.find_elements_by_css_selector(".checkbox")
        for check in checks:
            if check.text==u"医生":
                check.click()
                break
        driver.find_element_by_id("userDepartment").send_keys(u"骨外科")
        time.sleep(1)
        driver.find_element_by_id("userProfession").send_keys(u"医师")        
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
            addLog("员工管理新增员工测试成功")
        else:
            raise NameError(u"员工管理新增员工测试失败！")        

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()