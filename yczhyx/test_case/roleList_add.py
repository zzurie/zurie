# -*- coding: utf-8 -*-

import sys
sys.path.append("\public")
from public import *
import time,unittest
from selenium import webdriver
import string

class roleList_add(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.base_url="http://192.168.1.252:8010/WebSystem/login.aspx"
        self.verificationErrors=[]
        self.assert_next_alert=True
        self.driver.maximize_window()   
        
    def test_roleList_add(self):
        u"""新增角色、删除角色测试"""
        addLog("新增角色测试")
        driver=self.driver
        #打开角色管理页面
        #login().login(driver,self.base_url)
        login().login(driver)
        openMenu().openMenu(driver,u"权限管理",u"角色管理")
        #driver.get(self.base_url)
        #driver.find_element_by_id("userAccount").clear()
        #driver.find_element_by_id("userAccount").send_keys("admin")
        #driver.find_element_by_id("password").clear()
        #driver.find_element_by_id("password").send_keys("123456")
        #driver.find_element_by_xpath("//div[2]/form/div[4]/button").click() 
        #time.sleep(2)        
        #titles=driver.find_elements_by_css_selector(".title")
        #for title in titles:
            #if title.text==u"权限管理":
                #title.click()
        #time.sleep(2)
        #driver.find_element_by_link_text(u"角色管理").click()
        #time.sleep(2) 
        
        #获取当前记录数
        driver.switch_to_frame("main")
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        #print u"初始数目："+linetext
        n=linetext.find(u"。",0)
        line1=linetext[9:n-2]
        print line1
        
        #点击新增按钮,新增信息
        driver.find_element_by_id("sample_editable_1_new").click()
        driver.switch_to_default_content()
        time.sleep(2)
        driver.switch_to_frame("main")
        driver.find_element_by_id("rolename").send_keys(u"测试角色")
        driver.find_element_by_id("rolemark").send_keys(u"测试角色描述")
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.green").click()
        time.sleep(2)
        
        #获取新增后的记录数，判断是否新增角色成功
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        #print u"新增后数目："+linetext
        n=linetext.find(u"。",0)
        line2=linetext[9:n-2]        
        print line2
        if int(line2)==int(line1)+1:
            print u"新增成功"
            addLog("新增角色测试成功")
        else:
            raise NameError(u"新增角色失败！")
        
        ##删除新增的数据
        #xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        #table=getTable()
        #row=table.getRow(driver, xpath, u"测试角色")
        #row.click()
        ##删除得到的行
        #driver.find_element_by_id("btnDelete").click()
        #time.sleep(2)
        ##在弹出的确认删除对话框中点击是
        #btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        #time.sleep(2)
        #for btn in btns:
            #if btn.text==u"是":
                #btn.click()
        ##点击删除成功的提示
        #driver.find_element_by_css_selector(".l-dialog-btn-inner").click()
        time.sleep(5)
            
    def tearDown(self):
        self.driver.quit()
        self.assertEquals([], self.verificationErrors)
        
if __name__=="__main__":
    unittest.main()
