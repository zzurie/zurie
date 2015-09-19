# -*- coding: utf-8 -*-
import sys
sys.path.append("\public")
from public import *
from selenium import webdriver
import time
import unittest,re
from selenium.webdriver.common.by import By
import xlrd

class dictionary_edit(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="http://192.168.1.252:8010/websystem/login.aspx"
        self.driver.maximize_window()         

    def test_dictionary_edit(self):
        u"""字典维护修改字典测试"""
        addLog("字典维护修改字典测试")        
        driver=self.driver
        #打开字典维护页面
        login().login(driver)
        openMenu().openMenu(driver,u"系统设置",u"字典维护")
        
        #读取参数文件parameter.xls
        sheet=getParameter("dictionary")
        txt_name_old=sheet.cell(1,0).value
        txt_name=sheet.cell(2,0).value
        txt_code=sheet.cell(2,1).value
        txt_explain=sheet.cell(2,3).value
        
        #打开编辑页面
        driver.switch_to_frame("main")
        by_table=By.XPATH
        value_table=".//*[@id='maingridgrid']/div[4]/div[2]"
        by_page=By.XPATH
        value_page=".//*[@id='maingrid']/div[6]/div/div[8]/div[1]/span"
        numlist=findInPage().findRowNumBy(driver,by_table,value_table,by_page,value_page,txt_name_old,1)
        print numlist
        if numlist==None:
            print u"修改字典失败:没有找到"
            addLog("字典维护修改字典测试失败：没有找到要修改的字典")
            return
        pagenum=numlist[0]
        rownum=numlist[1]            
        #选中要修改信息所在行的复选框
        #翻页，直到页码pagenum
        #page=1
        #while page<int(pagenum):
            #driver.find_element_by_xpath(value_page).click()
            #page=page+1  
        findInPage().findPage(driver,by_page,value_page,pagenum)
        checks=driver.find_elements_by_css_selector(".l-grid-row-cell-btn-checkbox")
        checks[int(rownum)-1].click()                  
        #打开修改页面
        driver.find_element(by=By.CSS_SELECTOR,value="div.l-icon.l-icon-modify").click()
        time.sleep(1)
        
        #切换到修改frame
        frame=driver.find_element_by_xpath("//*[contains(@name,'igerwindow')]")
        driver.switch_to_frame(frame)
        driver.find_element_by_id("txt_name").clear()
        driver.find_element_by_id("txt_name").send_keys(txt_name)
        time.sleep(1)
        driver.find_element_by_id("txt_code").clear()
        driver.find_element_by_id("txt_code").send_keys(int(txt_code))
        time.sleep(1)
        driver.find_element_by_id("txt_explain").clear()
        driver.find_element_by_id("txt_explain").send_keys(txt_explain)
        time.sleep(2)
        driver.find_element_by_css_selector(".btn.blue").click()
        time.sleep(5)      
        
        #判断修改是否成功
        row=findInPage().findRowBy(driver,by_table,value_table,by_page,value_page,txt_name,1)
        if type(row)==NoneType:
            addLog("字典维护修改字典测试失败,没有找到修改后的信息")
        else:
            addLog("字典维护修改字典测试成功")               

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()