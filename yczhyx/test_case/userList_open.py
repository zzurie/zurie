# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest
from types import *

class userList_open(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_userList_open(self):
        u"""员工管理员工启用测试"""
        addLog("员工管理员工启用测试")        
        driver=self.driver
        #打开员工管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"员工管理",u"员工列表")
        
        #选中要启用的行复选框
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        numlist=findInPage().findRowNum(driver,xpath,u"newuseredit",2)
        print numlist
        if numlist==None:
            print u"员工启用失败：没有找到"
            addLog("员工管理员工启用测试失败：没有找到要启用的员工")
            return
        pagenum=numlist[0]
        rownum=numlist[1]
        #选中要员工启用所在行的复选框
        #先找到所在页面，再选中
        page=1
        while page<int(pagenum):
            driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
            page=page+1
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()    
        #点击启用按钮
        driver.find_element_by_id("btnUserOpen").click()
        time.sleep(2)
        
        #在弹出的确认启用对话框中点击是
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"是":
                btn.click()
        time.sleep(2)
        #点击启用成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()        
        
        #判断启用是否成功
        statusText=findInPage().findCellText(driver,xpath,(rownum,8))
        if statusText==u"已启用":
            addLog("员工管理员工启用测试成功")
        else:
            addLog("员工管理员工启用测试失败")             

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()