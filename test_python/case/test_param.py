"""
    目标：回顾parameterized参数化组件使用
    安装：pip install paramterized
    使用：@paramterized.expant(参数)
         参数：单个参数格式：列表 如：[值1，值2]
               多个参数：列表嵌套元组：如：[(参1值，参2值),(参3值，参4值)]
    需求：
        输入用户名密码，数据分别为：1.admin,123456 2.user002,654321
"""


#导包
import unittest
from parameterized import parameterized

#新建测试类
class TestParam(unittest.TestCase):
    #新建测试方法
    @parameterized.expand([("admin","123456"),("test","test123")])
    def test_para(self,username,password):
        print("用户名：",username)
        print("密码：",password)

if __name__ == '__main__':
    unittest.main()