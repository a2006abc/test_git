import json

# #打开json文件,并获取文件流
# with open('..\data\login.json','r',encoding='utf-8') as f:
#     #调用load方法加载文件流
#     data = json.load(f)
#     print(data)
#
# #使用函数进行封装
# def read_json():
#     with open('..\data\login.json','r',encoding='utf-8') as f:
#         data = json.load(f)


class ReadJson():
    def __init__(self,filename):
        self.filepath = "../data/"+filename
    def read_json(self):
        with open(self.filepath,'r',encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    print(ReadJson('login.json').read_json())
    #登录数据调用
    data = ReadJson('login.json').read_json()
    print(type(data))
    #新建一个空列表读取json数据
    arrs=[]
    arrs.append((data.get('url'),
                 data.get('username'),
                 data.get('password'),
                 data.get('Submit')))
    print(arrs)
