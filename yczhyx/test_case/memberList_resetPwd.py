# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest

class memberList_resetPwd(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        #self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_memberList_resetPwd(self):
        u"""会员管理密码重置测试"""
        addLog("会员管理密码重置测试")        
        driver=self.driver
        #打开会员管理页面
        #login().login(driver,self.url)
        login().login(driver)
        openMenu().openMenu(driver,u"会员管理",u"会员列表")
       
        #选中要密码重置的行复选框
        driver.switch_to_frame("main")
        xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
        try:
            row=findInPage().findRow(driver,xpath,"huiyuan5",1)
            row.click()
        except AttributeError,msg:
            print u"编辑会员失败："+msg.message
            addLog("会员管理编辑会员测试失败：没有找到要编辑的会员")
            return   
        #点击密码重置按钮
        editCell=findInPage().findCell(row,8)
        editCell.click()         
   
        #在弹出的确认对话框中点击是
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"是":
                btn.click()
        time.sleep(2)
        #点击成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()                 
            
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()