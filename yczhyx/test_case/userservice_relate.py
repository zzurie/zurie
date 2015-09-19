# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time

class userservice_relate(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()
        
    def test_userservice_del(self):
        u"""服务管理关联服务级别测试"""
        addLog("服务管理关联服务级别测试")
        #打开服务管理页面
        driver=self.driver
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"系统设置",u"服务管理")
        
        #选中要关联服务级别的服务
        #先得到要关联服务级别服务所在的行号，从而选中checkbox
        #参数numlist:调用findInPage类中的finRowNum函数，获取元素所在的页面、行号
        #参数pagenum:页码数
        #参数rownum:行号
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        numlist=findInPage().findRowNum(driver,xpath,u"新增服务修改",2)
        print numlist
        if numlist==None:
            #row=findInPage().findRow(driver,xpath,u"新增服务修改",1)
            print u"关联服务级别服务失败:没有找到"
            addLog("服务管理关联服务级别测试失败：没有找到要关联服务级别的服务")
            return
        pagenum=numlist[0]
        rownum=numlist[1]
        #选中要关联服务级别服务所在行的复选框
        #翻页，直到页码pagenum
        page=1
        while page<int(pagenum):
            driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
            page=page+1
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()   
        driver.find_element_by_id("Button5").click()
        
        #在弹出的窗口中选择要关联的服务级别
        driver.switch_to_frame(driver.find_element_by_css_selector(".l-dialog-content iframe"))
        driver.find_element_by_id("userlevelList").send_keys(u"一级服务")
        #在弹出的对话框中点击确认
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"确认":
                btn.click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        #点击关联服务级别成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()        
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()