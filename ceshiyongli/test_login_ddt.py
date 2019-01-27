from selenium import webdriver
import unittest
import ddt
import os
from WebZidong2.pages.login_page import LoginPage,login_url
from WebZidong2.common.read_excel import ExcelUtil
'''
1输入 账号admin 输入密码123456 点击登录
2输入 账号admin 不输入密码 点击登录
3输入 账号admin 输入密码123456 点击记住登录  点击登录
'''
#测试的数据
# testdates=[
#     {"user":"admin" ,"psw":"123456","expect":"admin"},
#     {"user":"admin" ,"psw":"","expect":""},
#     {"user":"admin11" ,"psw":"123456","expect":""},
# ]
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath, "common", "datas.xlsx")
print(filepath)
#filepath = r"F:\软件测试前端实例\\untitled\WebZidong2\common\datas.xlsx"
data = ExcelUtil(filepath)
testdates = data.dict_data()
print(testdates)
@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login =LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.login.is_alert_exists()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self,user,psw,expect):
        self.login.login(user,psw)
        result = self.login.get_login_name()
        print("测试结果：%s" % result)
        self.assertTrue(result == expect)

    # @ddt.data({"user": "admin", "psw": "123456", "expect": "admin"},
    # {"user": "admin", "psw": "", "expect": ""},
    # {"user": "admin11", "psw": "123456", "expect": ""},)
    @ddt.data(*testdates) #相当于上面的
    def test_01(self,data):
        '''输入账号admin输入密码123456点击登录'''
        print("------------开始测试------------")
        print("测试数据%s" % data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("------------结束:pass-------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":

  unittest.main()