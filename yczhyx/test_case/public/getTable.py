# -*- coding: utf-8 -*-
#本文档用于获取页面table控件中的行、元素
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
import time


class getTable(object):
    def __init__(self):
        #print "init"
        pass
        
    #从一个table的单元格中得到文本值. 
    #参数tableCellAddress为一个元组, 行列从1开始,标记一个单元格地址, 如. "（1，4）"
    #参数xpath 用于得到table对象
    #return 从一个table的单元格中得到文本值
    def getCellText(self,mydriver,xpath,tableCellAddress):
        #得到table元素对象
        driver=mydriver
        table=driver.find_element_by_xpath(xpath)
        #对所要查找的单元格位置字符串进行分解，得到其对应行、列。
        row=tableCellAddress[0]
        cell=tableCellAddress[1]
        #得到table表中所有行对象，并得到所要查询的行对象。
        rows=table.find_elements_by_tag_name("tr")
        therow=rows[row-1]
        #调用getCell方法得到对应的列对象，然后得到要查询的文本
        text=self.getCell(therow,cell).text
        return text
        
        
    #从一个table的单元格中得到文本值. 
    #return 从一个table的单元格中得到文本值
    def getCellTextBy(self,mydriver,by_table,value_table,tableCellAddress):
        #得到table元素对象
        driver=mydriver
        table=driver.find_element(by=by_table,value=value_table)
        #对所要查找的单元格位置字符串进行分解，得到其对应行、列。
        row=tableCellAddress[0]
        cell=tableCellAddress[1]
        #得到table表中所有行对象，并得到所要查询的行对象。
        rows=table.find_elements_by_tag_name("tr")
        therow=rows[row-1]
        #调用getCell方法得到对应的列对象，然后得到要查询的文本
        text=self.getCell(therow,cell).text
        return text
    
    #从一个table的单元格中得到某一行，以第二列的元素判断是否是需要的行
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始 
    #参数xpath 用于得到table对象
    #return 返回要查找的行信息
    def getRow(self,mydriver,xpath,cellText,cellNum):
        #得到table元素对象
        driver=mydriver
        table=driver.find_element_by_xpath(xpath)
        #得到table表中所有行对象，并得到所要查询的行对象。
        rows=table.find_elements_by_tag_name("tr")
        for row in rows:
            if self.getCell(row,cellNum).text==cellText:
                return row 
            
    #从一个table的单元格中得到某一行，以第二列的元素判断是否是需要的行
    #参数by_table：By的实例，表明table的find_element的参数
    #参数value_table：by_table的value
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始    
    #return 返回要查找的行信息
    def getRowBy(self,mydriver,by_table,value_table,cellText,cellNum):
        #得到table元素对象
        driver=mydriver
        #table=driver.find_element_by_xpath(xpath)
        table=driver.find_element(by=by_table,value=value_table)
        #得到table表中所有行对象，并得到所要查询的行对象。
        rows=table.find_elements_by_tag_name("tr")
        for row in rows:
            if self.getCell(row,cellNum).text==cellText:
                return row 
    
    #得到包含某个信息的行所在的行号
    #从一个table的单元格中得到某一行，以第二列的元素判断是否是需要的行
    #参数cellText：元素信息
    #参数cellNum：元素所在的列号，从1开始
    #参数xpath 用于得到table对象
    #return 返回要查找的行信息
    def getRowNum(self,mydriver,xpath,cellText,cellNum):
        #得到table元素对象
        driver=mydriver
        table=driver.find_element_by_xpath(xpath)
        #得到table表中所有行对象，并得到所要查询的行对象。
        rows=table.find_elements_by_tag_name("tr")
        num=1
        for row in rows:
            if self.getCell(row,cellNum).text==cellText:
                return num  
            else:
                num=num+1
                
    #得到包含某个信息的行所在的行号
    #从一个table的单元格中得到某一行，以第二列的元素判断是否是需要的行
    #参数by_table：By的实例，表明table的find_element的参数
    #参数value_table：by_table的value
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始 
    #return 返回要查找的行信息
    def getRowNumBy(self,mydriver,by_table,value_table,cellText,cellNum):
        #得到table元素对象
        driver=mydriver
        table=driver.find_element(by=by_table,value=value_table)
        #得到table表中所有行对象，并得到所要查询的行对象。
        rows=table.find_elements_by_tag_name("tr")
        num=1
        for row in rows:
            if self.getCell(row,cellNum).text==cellText:
                return num  
            else:
                num=num+1
                
    #获取指定列的元素
    #Row:行元素
    #cell:列的数值,从1开始
    #返回指定单元格的元素    
    def getCell(self,row,cell):

        #列里面有"<th>"、"<td>"两种标签，所以分开处理。
        #if row.find_element_by_tag_name("th").size>0:
            #cells=row.find_element_by_tag_name("th")
            #target=cells[cell]
        if row.find_element_by_tag_name("td").size>0:
            cells=row.find_elements_by_tag_name("td")
            target=cells[cell-1]
        return target  
    
    def initTable(self):
        self.driver=webdriver.Chrome()
        url="http://192.168.1.252:8010/WebSystem/login.aspx"
        self.driver.get(url)
        self.driver.maximize_window()
        
        self.driver.find_element_by_id("userAccount").clear()
        self.driver.find_element_by_id("userAccount").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//div[2]/form/div[4]/button").click()
        time.sleep(2)            
        titles=self.driver.find_elements_by_css_selector(".title")
        for title in titles:
            if title.text==u"权限管理":
                title.click()
        time.sleep(2)
        self.driver.find_element_by_link_text(u"角色管理").click()
        time.sleep(2)     
        self.driver.switch_to_frame("main")   
        return self.driver  
    
    def __del__(self):
        #print "end getTable"
        pass

if __name__=="__main__":
    table=getTable()
    xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
    driver=table.initTable()
    text=table.getCellText(driver,xpath, (2,2))
    num=table.getRowNum(driver, xpath, u"医生", 1)
    print num
    print text
    driver.quit()
