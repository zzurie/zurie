# -*- coding: utf-8 -*-
#本文档用于翻页查找页面table控件中的行以及元素
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
import time
from getTable import getTable
from types import *

class findInPage(object):
    def __init__(self):
        pass
    
    #返回table中指定列内容的行元素
    #参数xpath:table的xpath路径
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始
    def findRow(self,mydriver,xpath,cellText,cellNum):
        driver=mydriver
        table=getTable()
        #获取分页数目
        num=driver.find_element_by_css_selector(".pcontrol").text[2]
        for pageNum in range(1,int(num)+1):
            print pageNum
            row=table.getRow(driver, xpath, cellText, cellNum)
            if type(row)==NoneType:
                pageNum=pageNum+1
                driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
                time.sleep(2)
                #driver.find_element_by_css_selector(".l-bar-button.l-bar-btnnext.l-bar-button-over>span").click()
            else:
                return row
        
            
    #返回table中指定列内容的行元素
    #参数by_table：By的实例，表明table的find_element的参数
    #参数value_table：by_table的value
    #参数by_page：By的实例，表明翻页控件page的find_element的参数
    #参数value_page：by_page的value    
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始
    def findRowBy(self,mydriver,by_table,value_table,by_page,value_page,cellText,cellNum):
        driver=mydriver
        table=getTable()
        #获取分页数目
        num=driver.find_element_by_css_selector(".pcontrol").text[2]
        for pageNum in range(1,int(num)+1):
            print pageNum
            row=table.getRowBy(driver, by_table,value_table, cellText, cellNum)
            if type(row)==NoneType:
                pageNum=pageNum+1
                #driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
                driver.find_element(by=by_page,value=value_page).click()
                time.sleep(2)
                #driver.find_element_by_css_selector(".l-bar-button.l-bar-btnnext.l-bar-button-over>span").click()
            else:
                return row
            
    #获取指定列的元素
    #Row:行元素
    #cell:指定列的数值，从1开始
    #返回指定单元格的元素    
    def findCell(self,row,cellnum):     
        #列里面有"<th>"、"<td>"两种标签，所以分开处理。
        #if row.find_element_by_tag_name("th").size>0:
        #cells=row.find_element_by_tag_name("th")
        #target=cells[cell]
        if row.find_element_by_tag_name("td").size>0:
            cells=row.find_elements_by_tag_name("td")
            target=cells[cellnum-1]
            return target     
    
    #翻页查找指定元素的页码、行号 
    #从一个table的单元格中得到某一行，以第二列的元素判断是否是需要的行   
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始    
    #return 返回要查找的行信息
    def findRowNum(self,mydriver,xpath,cellText,cellNum):
        #得到table元素对象
        driver=mydriver
        table=getTable()
        #获取分页数目
        num=driver.find_element_by_css_selector(".pcontrol").text[2]  
        for page in range(1,int(num)+1):
            print page
            rownum=table.getRowNum(mydriver, xpath, cellText, cellNum)
            if type(rownum)==NoneType:
                page=page+1
                driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
                time.sleep(2) 
            else:
                return (page,rownum)
            
            
    #翻页查找指定元素的页码、行号 
    #从一个table的单元格中得到某一行，以第二列的元素判断是否是需要的行
    #参数by_table：By的实例，表明table的find_element的参数
    #参数value_table：by_table的value
    #参数by_page：By的实例，表明翻页控件page的find_element的参数
    #参数value_page：by_page的value    
    #参数cellText：指定列的内容
    #参数cellNum：指定列的列号，从1开始    
    #return 返回要查找的行信息
    def findRowNumBy(self,mydriver,by_table,value_table,by_page,value_page,cellText,cellNum):
        #得到table元素对象
        driver=mydriver
        table=getTable()
        #获取分页数目
        num=driver.find_element_by_css_selector(".pcontrol").text[2]  
        for page in range(1,int(num)+1):
            print page
            rownum=table.getRowNumBy(mydriver,by_table,value_table,cellText, cellNum)
            if type(rownum)==NoneType:
                page=page+1
                #driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
                driver.find_element(by=by_page,value=value_page).click()
                time.sleep(2) 
            else:
                return (page,rownum)
    
    def findCellText(self,mydriver,table_xpath,page_xpath,pagenum,tableCellAddress):
        #得到table元素对象
        driver=mydriver
        table=getTable()
        #翻页，一直到pagenum页面
        nowpage=self.findNowPage(driver)
        if nowpage==pagenum:
            pass
        else:
            page=1
            while page<pagenum:
                page=page+1
                driver.find_element_by_xpath(page_xpath).click()
                time.sleep(1)
        text=table.getCellText(driver, table_xpath, tableCellAddress)    
        return text                  
    
    def findCellTextBy(self,mydriver,by_table,value_table,by_page,value_page,pagenum,tableCellAddress):
        #得到table元素对象
        driver=mydriver
        table=getTable()
 
        #翻页，一直到pagenum页面
        nowpage=self.findNowPage(driver)
        if nowpage==pagenum:
            pass
        else:
            page=1
            while page<pagenum:
                page=page+1
                driver.find_element_by_xpath(value_page).click()
                time.sleep(1)
        text=table.getCellTextBy(driver, by_table,value_table, tableCellAddress)          
        return text
    
    #参数row：行元素
    #参数cellnium：列元素的数值，从1开始
    def findCellTextInRow(self,row,cellnum):
        #调用findCell方法得到对应的列对象，然后得到要查询的文本
        text=self.findCell(row,cellnum).text
        return text  
    
    #获取总的记录数
    def findTotalNum(self,mydriver):
        driver=mydriver
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        #print linetext
        m=linetext.find(u"总",0)
        n=linetext.find(u"条",0) #n:“。”的序号
        #print n
        #linenum 总的记录数
        totalNum=linetext[m+1:n]
        print u"总的记录数："+totalNum
        return int(totalNum)
    
    #获取总的页码数
    #linenum：总的记录数
    #pagenum：每页显示的记录数
    #返回值nowpage
    def findTotalPage(self,mydriver):
        driver=mydriver
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        #print linetext
        #pagenum 每页显示数目
        n=linetext.find(u"。",0) #n:“。”的序号
        m=linetext.find(u"：",n)   #m：第二个：所在的序号
        pagenum=linetext[m+1:]
        #print u"每页显示的数目："+pagenum
        x=linetext.find(u"总",0)
        y=linetext.find(u"条",0) #n:“。”的序号
        #totalNum 总的记录数
        totalNum=linetext[x+1:y]
        #print u"总的记录数："+totalNum
        totalPage=int(totalNum)/int(pagenum)
        num=float(totalNum)/float(pagenum)
        print int(num)
        return totalPage
    

    #获取当前所在的页码数
    #linenum：总的记录数
    #pagenum：每页显示的记录数
    #返回值nowpage    
    def findNowPage(self,mydriver):
        driver=mydriver
        linetext=driver.find_element_by_css_selector(".l-bar-text").text
        #print linetext
        #pagenum 每页显示数目
        n=linetext.find(u"。",0) #n:“。”的序号
        m=linetext.find(u"：",n)   #m：第二个：所在的序号
        #print m
        pagenum=linetext[m+1:]
        #print u"每页显示的数目："+pagenum
        x=linetext.find(u"到",0)
        y=linetext.find(u"，",0)  #y：第一个"，"所在的序号
        #print x,y
        nowpagenum=linetext[x+1:y]
        #print u"当前页面显示到的记录数："+nowpagenum
        nowPage=int(nowpagenum)/int(pagenum)
        return nowPage    
        
    #翻页，一直到指定页面
    def findPage(self,mydriver,by_page,page_xpath,pagenum):
        #得到table元素对象
        driver=mydriver
        table=getTable()
        #翻页，一直到pagenum页面
        nowpage=self.findNowPage(driver)
        if nowpage==pagenum:
            pass
        else:
            page=1
            while page<pagenum:
                page=page+1
                driver.find_element(by=by_page,value=page_xpath).click()
                time.sleep(1)
                
    def initPage(self):
        #用于本文档测试
        self.driver=webdriver.Chrome()
        self.url="http://192.168.1.252:8010/WebSystem/login.aspx"
        self.driver.get(self.url)
        self.driver.maximize_window()
        
        self.driver.find_element_by_id("userAccount").clear()
        self.driver.find_element_by_id("userAccount").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//div[2]/form/div[4]/button").click()
        time.sleep(2)            
        titles=self.driver.find_elements_by_css_selector(".title")
        for title in titles:
            if title.text==u"员工管理":
                title.click()
        time.sleep(2)
        self.driver.find_element_by_link_text(u"员工列表").click()
        time.sleep(2)     
        self.driver.switch_to_frame("main")   
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='maingrid']/div[5]/div/div[8]/div[1]/span").click()
        return self.driver
    
    def __del__(self):
        pass
    
if __name__=="__main__":
    find=findInPage()
    driver=find.initPage()
    xpath=".//*[@id='maingridgrid']/div[4]/div[2]"
    cellText=u"usertest1"
    cellNum=0
    #row=find.findRow(driver,xpath, cellText, cellNum)
    #row.click()
    #numlist=find.findRowNum(driver, xpath, cellText, cellNum)
    #print numlist
    page=find.findNowPage(driver)
    #print page
    totalnum=find.findTotalNum(driver)
    #print totalnum
    totalpage=find.findTotalPage(driver)
    print totalpage
    driver.quit()