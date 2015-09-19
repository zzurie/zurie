# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest,re
from selenium.webdriver.common.by import By
import xlrd

class dictionary_add(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_dictionary_add(self):
        u"""字典维护增加字典测试"""
        addLog("字典维护增加字典测试")        
        driver=self.driver
        #打开字典维护页面
        login().login(driver)
        openMenu().openMenu(driver,u"系统设置",u"字典维护")
    
        #读取参数文件parameter.xls
        sheet=getParameter("dictionary")
        txt_name=sheet.cell(1,0).value
        txt_code=sheet.cell(1,1).value
        sel_type=sheet.cell(1,2).value
        txt_explain=sheet.cell(1,3).value
        txt_remark=sheet.cell(1,4).value
        #print txt_name+sel_type+txt_explain+txt_remark
        
        #获取当前记录数
        driver.switch_to_frame("main")
        line1=findInPage().findTotalNum(driver)
    
        driver.find_element(by=By.CSS_SELECTOR,value="div.l-icon.l-icon-add").click()
        time.sleep(1)
        
        #切换到增加frame
        frame=driver.find_element_by_xpath("//*[contains(@name,'igerwindow')]")
        driver.switch_to_frame(frame)
        driver.find_element_by_id("txt_name").send_keys(txt_name)
        time.sleep(1)
        driver.find_element_by_id("txt_code").send_keys(int(txt_code))
        time.sleep(1)
        driver.find_element_by_id("sel_type").send_keys(sel_type)
        time.sleep(1)
        driver.find_element_by_id("txt_explain").send_keys(txt_explain)
        time.sleep(1)
        driver.find_element_by_id("txt_remark").send_keys(txt_remark)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)
        
        driver.switch_to_default_content()
        driver.switch_to_frame("main")
        line2=findInPage().findTotalNum(driver)
        if int(line2)==int(line1)+1:
            #print u"新增成功"
            addLog("字典维护增加字典测试成功")
        else:
            addLog(u"字典维护增加字典测试失败！")        

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()