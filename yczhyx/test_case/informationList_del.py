# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest
from types import *
from selenium.webdriver.common.by import By

class informationList_del(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_informationList_del(self):
        u"""资讯管理删除资讯测试"""
        addLog("资讯管理删除资讯测试")        
        driver=self.driver
        #打开资讯管理页面
        login().login(driver)
        openMenu().openMenu(driver,u"网站管理",u"资讯管理")
        
        #获取当前记录数
        driver.switch_to_frame("main")
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"初始数目："+linetext
        n=linetext.find(u"。",0)
        line1=linetext[9:n-2]
        print line1        
    
        #选中要删除的行
        by_table=By.XPATH
        by_page=By.XPATH
        value_table=".//*[@id='maingridgrid']/div[4]/div[2]"  
        value_page=".//*[@id='maingrid']/div[6]/div/div[8]/div[1]/span"
        try:
            row=findInPage().findRowBy(driver,by_table,value_table,by_page,value_page,u"新增资讯修改",1)
            row.click()
        except AttributeError,msg:
            print u"删除失败："+msg.message
            addLog("资讯管理删除资讯测试失败：没有找到要删除的资讯")
            return
        #点击删除按钮,删除信息
        #driver.find_element_by_css_selector(".l-toolbar-item.l-panel-btn.l-toolbar-item-hasicon.l-panel-btn-over>span").click()
        driver.find_element_by_xpath(".//*[@id='maingrid']/div[3]/div/div[5]/span").click()
        #在弹出的确认删除对话框中点击是
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"是":
                btn.click()
        time.sleep(2)
        #点击删除成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()       

        #获取删除后的记录数，判断是否删除成功
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"删除后数目："+linetext
        n=linetext.find(u"。",0)
        line2=linetext[9:n-2]        
        print line2
        if int(line2)==int(line1)-1:
            print u"删除成功"
            addLog("资讯管理删除资讯测试成功")
        else:
            raise NameError(u"资讯管理删除资讯测试失败！")   
            
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()