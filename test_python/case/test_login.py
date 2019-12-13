import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

def get_data():
    data = ReadJson('login.json').read_json()
    print(type(data))
    #新建一个空列表读取json数据
    arrs=[]
    arrs.append((data.get('url'),
                 data.get('username'),
                 data.get('password'),
                 data.get('Submit')))
    return arrs
#创建测试类
class TestLogin(unittest.TestCase):
    #创建测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,username,password,Submit):
        #临时数据
        # url = 'http://127.0.0.1:8080/jenkins/j_acegi_security_check'
        # username='hz_wjping'
        # password='A2008abc'
        # Submit=u'登录'
        #调用测试类
        s = ApiLogin.api_post_login(url,username,password,Submit)
        #查看结果
        print(s.content.decode('utf-8'))
        #断言

if __name__ == '__main__':
    unittest.main()