# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest
from types import *

class userList_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_userList_edit(self):
        u"""员工管理编辑员工测试"""
        addLog("员工管理编辑员工测试")        
        driver=self.driver
        #打开员工管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"员工管理",u"员工列表")
        
        #选中要编辑的行复选框
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        numlist=findInPage().findRowNum(driver,xpath,"yuangong",2)
        print numlist
        if numlist==None:
            print u"员工编辑失败：没有找到"
            addLog("员工管理编辑员工测试失败：没有找到要编辑的员工")
            return
        pagenum=numlist[0]
        rownum=numlist[1]
        #选中要编辑员工所在行的复选框
        #先找到所在页面，再选中
        page=1
        while page<int(pagenum):
            driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
            page=page+1
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()    
        #点击编辑按钮
        driver.find_element_by_id("Button1").click()
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        #driver.find_element_by_id("userCode").send_keys("gonghao")
        #time.sleep(1)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(u"新增员工修改")
        time.sleep(1)
        #driver.find_element_by_id("userSex").send_keys(u"女")
        #time.sleep(1)
        #driver.find_element_by_id("useHospital").send_keys(u"济南市中心医院")
        #time.sleep(1)
        driver.find_element_by_id("userAccount").clear()
        driver.find_element_by_id("userAccount").send_keys("newuseredit")
        time.sleep(1)
        #driver.find_element_by_id("userPwd").send_keys("123456")
        #time.sleep(1)
        #driver.find_element_by_id("userDepartment").send_keys(u"骨外科")
        #time.sleep(1)
        #driver.find_element_by_id("userProfession").send_keys(u"医师")        
        #time.sleep(2)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)
    
        #判断是否修改成功
        row=findInPage().findRow(driver, xpath, u"newuseredit",2)
        if type(row)==NoneType:
            addLog("员工管理编辑员工测试失败，没有找到编辑后的信息")
        else:
            addLog("员工管理编辑员工测试成功")      

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()