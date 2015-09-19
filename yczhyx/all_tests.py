# -*- coding: utf-8 -*-
import sys
sys.path.append("\test_case")
from test_case import *
import unittest,time
import HTMLTestRunner

testunit=unittest.TestSuite()
#将测试用例加入到测试容器中
#testunit.addTest(unittest.makeSuite(login.login))
#testunit.addTest(unittest.makeSuite(roleList_add.roleList_add))
#testunit.addTest(unittest.makeSuite(roleList_distribute.roleList_distribute))
#testunit.addTest(unittest.makeSuite(roleList_viewDistribution.roleList_viewDistribution))
#testunit.addTest(unittest.makeSuite(roleList_edit.roleList_edit))
#testunit.addTest(unittest.makeSuite(roleList_del.roleList_del))
#testunit.addTest(unittest.makeSuite(userservice_add.userservice_add))
#testunit.addTest(unittest.makeSuite(userservice_edit.userservice_edit))
#testunit.addTest(unittest.makeSuite(userservice_del.userservice_del))
#testunit.addTest(unittest.makeSuite(userservice_open.userservice_open))
#testunit.addTest(unittest.makeSuite(userservice_relate.userservice_relate))
#testunit.addTest(unittest.makeSuite(userList_add.userList_add))
#testunit.addTest(unittest.makeSuite(userList_edit.userList_edit))
#testunit.addTest(unittest.makeSuite(userList_del.userList_del))
#testunit.addTest(unittest.makeSuite(userList_open.userList_open))
#testunit.addTest(unittest.makeSuite(userList_assistant.userList_assistant))
#testunit.addTest(unittest.makeSuite(depList_add.depList_add))
#testunit.addTest(unittest.makeSuite(depList_edit.depList_edit))
#testunit.addTest(unittest.makeSuite(depList_del.depList_del))                 
testunit.addTest(unittest.makeSuite(InformationList_add.informationList_add))
testunit.addTest(unittest.makeSuite(informationList_edit.informationList_edit))
testunit.addTest(unittest.makeSuite(informationList_del.informationList_del))

now=time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
#t=time.strftime("%Y%m%d-%H%M%S")
#定义报告存放路径
filename="f:\\learn\\yczhyx\\report\\"+now+"result.html"
fp=file(filename,'wb')

#定义测试报告
runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u"院外管理系统后台自动化测试报告",
    description=u"用例执行情况：")

#执行测试套件
#runner=unittest.TextTestRunner()
#runner.run(testunit)

runner.run(testunit)
