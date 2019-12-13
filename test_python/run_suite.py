import HtmlTestRunner
import time
import unittest

#第一步 组长测试套件
suite= unittest.defaultTestLoader.discover("./case",pattern="test*.py")

#第二部 指定测试报告存放路径及文件名称
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
#第三步：运行测试套件并生成测试报告
with open(file_path,"wb")as f:
    HtmlTestRunner(stream = f).run(suite)