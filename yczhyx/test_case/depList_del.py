# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import unittest,time
from types import *

class depList_del(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()  
        
    def test_depList_del(self):
        u"""部门管理删除部门测试"""
        addLog("部门管理删除部门测试")
        driver=self.driver
        #打开部门管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"权限管理",u"部门管理")
        
        #获取当前记录数
        driver.switch_to_frame("main")
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        print u"初始数目："+linetext
        n=linetext.find(u"。",0)
        line1=linetext[9:n-2]
        print line1        

        #选中记录
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        try:
            row=findInPage().findRow(driver,xpath,u"新增部门修改",2)
            row.click()
        except AttributeError,msg:
            print u"删除部门失败："+msg.message
            addLog("部门管理删除部门测试失败：没有找到要删除的部门")
            return
        #点击删除按钮
        driver.find_element_by_id("btnDelete").click()  
        time.sleep(2)
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
        line2=linetext[10:n-2]        
        print line2
        if int(line2)==int(line1)-1:
            print u"删除成功"
            addLog("部门管理删除部门测试成功")
        else:
            raise NameError(u"部门管理删除部门测试失败！")   
            
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()