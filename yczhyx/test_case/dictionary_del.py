# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest,re
from selenium.webdriver.common.by import By

class dictionary_del(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_dictionary_del(self):
        u"""字典维护删除字典测试"""
        addLog("字典维护删除字典测试")        
        driver=self.driver
        #打开字典维护页面
        login().login(driver)
        openMenu().openMenu(driver,u"系统设置",u"字典维护")
        
        #找到要删除的行
        driver.switch_to_frame("main")
        by_table=By.XPATH
        value_table=".//*[@id='maingridgrid']/div[4]/div[2]"
        by_page=By.XPATH
        value_page=".//*[@id='maingrid']/div[6]/div/div[8]/div[1]/span"
        numlist=findInPage().findRowNumBy(driver,by_table,value_table,by_page,value_page,u"新增字典",1)
        print numlist
        if numlist==None:
            print u"删除字典失败:没有找到"
            addLog("字典维护删除字典测试失败：没有找到要删除的字典")
            return
        pagenum=numlist[0]
        rownum=numlist[1]            
        #选中要启用服务所在行的复选框
        #翻页，直到页码pagenum
        findInPage().findPage(driver,by_page,value_page,pagenum)
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()       
        
        #点击删除按钮
        driver.find_element(by=By.XPATH,value=".//*[@id='maingrid']/div[3]/div/div[5]/span").click()
        time.sleep(1)
        
        #在弹出的确认对话框中点击是
        btns=driver.find_elements_by_css_selector(".l-dialog-btn-inner")
        time.sleep(2)
        for btn in btns:
            if btn.text==u"是":
                btn.click()
        time.sleep(5)
        #点击成功的提示
        driver.find_element_by_css_selector(".l-dialog-btn-inner").click()           
        
        #判断是否成功
        delstatus=findInPage().findCellTextBy(driver,by_table,value_table,by_page,value_page,pagenum,(rownum,6))
        if delstatus==u"已删除":
            addLog("字典维护删除字典测试成功")
        else:
            addLog("字典维护删除字典测试失败")               

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()