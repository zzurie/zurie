# -*- coding:utf-8 -*-
#本文档用于从Excel文件中读取参数信息
import sys,os
import xlrd


def getParameter(sheetname):
    #或者参数文件路径
    parentdir=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print parentdir
    #读取参数文件parameter.xls
    data=xlrd.open_workbook(parentdir+"\\data\\parameter.xls")
    sheet=data.sheet_by_name(sheetname) 
    return sheet

if __name__=="__main__":
    sheet=getParameter("dictionary")
    txt_name=sheet.cell(1,0).value
    print txt_name