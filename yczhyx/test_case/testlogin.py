# -*- coding: utf-8 -*-

from selenium import webdriver
import time,os,csv,unittest
import HTMLTestRunner

class login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="http://192.168.1.252:8010/websystem/login.aspx"
        self.verificationErrors=[]
        self.accept_next_alert=True

    def test_login(self):
        u"""登录测试"""
        driver=self.driver
        driver.maximize_window()
        self.driver.get(self.base_url)
        driver.find_element_by_id("userAccount").clear()
        driver.find_element_by_id("userAccount").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//div[2]/form/div[4]/button").click()
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    unittest.main()