# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest

class memberList_del(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_memberList_del(self):
        u"""会员管理禁用会员测试"""
        addLog("会员管理禁用会员测试")        
        driver=self.driver
        #打开会员管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"会员管理",u"会员列表")
       
        #选中要禁用的行复选框
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        numlist=findInPage().findRowNum(driver,xpath,"huiyuan5",1)
        print numlist
        if numlist==None:
            print u"会员禁用失败：没有找到"
            addLog("会员管理会员禁用测试失败：没有找到要禁用的会员")
            return
        pagenum=numlist[0]
        rownum=numlist[1]        
        #选中要员工禁用所在行的复选框
        #先找到所在页面，再选中
        page=1
        while page<int(pagenum):
            driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
            page=page+1
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()   
        
        #点击禁用按钮
        driver.find_element_by_id("btnUserDelete").click()
   
        #在弹出的确认禁用对话框中点击是
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"是":
                btn.click()
        time.sleep(2)
        #点击禁用成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()        
        
        #判断禁用是否成功
        statusText=findInPage().findCellText(driver,xpath,(rownum,5))
        if statusText==u"已禁用":
            addLog("会员管理会员禁用测试成功")
        else:
            addLog("会员管理会员禁用测试失败")            
            
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()