# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest
from types import *

class userList_assistant(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_userList_assistant(self):
        u"""员工管理指派助理测试"""
        addLog("员工管理指派助理测试")        
        driver=self.driver
        #打开员工管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"员工管理",u"员工列表")
           
        #点击指派助理按钮，打开指派助理页面
        driver.switch_to_frame("main")
        driver.find_element_by_id("Button5").click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        #选择助理
        driver.find_element_by_id("Assistant").send_keys("test[test111]")
        time.sleep(2)
        #选择医生
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        numlist=findInPage().findRowNum(driver,xpath,u"yuangong1",1)
        print numlist
        if numlist==None:
            print u"指派助理失败：没有找到"
            addLog("员工管理指派助理测试失败：没有找到要指派的医生")
            return
        pagenum=numlist[0]
        rownum=numlist[1]
        #选中要指派助理的医生所在行的复选框
        #先找到所在页面，再选中
        page=1
        while page<int(pagenum):
            driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
            page=page+1
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()    
        time.sleep(2)
        
        #确定指派
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        #判断指派助理是否成功
        statusText=findInPage().findCellText(driver,xpath,(rownum,9))
        if statusText=="test":
            addLog("员工管理指派助理测试成功")
        else:
            addLog("员工管理指派助理测试失败")             

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()