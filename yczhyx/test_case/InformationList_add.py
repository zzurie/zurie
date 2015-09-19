# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest

class informationList_add(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_informationList_add(self):
        u"""资讯管理新增资讯测试"""
        addLog("资讯管理新增资讯测试")        
        driver=self.driver
        #打开资讯管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"网站管理",u"资讯管理")
        
        #获取当前记录数
        driver.switch_to_frame("main")
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"初始数目："+linetext
        n=linetext.find(u"。",0)
        line1=linetext[9:n-2]
        print line1
    
        #点击新增按钮,新增信息
        driver.find_element_by_css_selector("div.l-icon.l-icon-add").click()
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("txtTitle").send_keys(u"新增资讯")
        time.sleep(1)
        driver.find_element_by_id("ConsultType").send_keys(u"健康资讯")
        time.sleep(1)
        driver.find_element_by_id("Summary").send_keys(u"新增资讯简介")
        time.sleep(1)
        
        driver.switch_to_frame("ueditor_0")
        #driver.find_element_by_css_selector("html.view body.view").click()
        driver.find_element_by_css_selector("html.view body.view").send_keys(u"新增资讯内容")
        time.sleep(1)
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)
        #在弹出的是否继续对话框中点击否
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"否":
                btn.click()
                break
        time.sleep(2)    
     
        #获取新增后的记录数，判断是否新增成功
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"新增后数目："+linetext
        n=linetext.find(u"。",0)
        line2=linetext[9:n-2]        
        print line2
        if int(line2)==int(line1)+1:
            print u"新增成功"
            addLog("资讯管理新增资讯测试成功")
        else:
            raise NameError(u"资讯管理新增资讯测试失败！")        

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()