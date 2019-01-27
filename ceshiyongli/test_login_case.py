from selenium import webdriver
import unittest

from WebZidong2.pages.login_page import LoginPage,login_url
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login =LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.login.is_alert_exists()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        '''输入账号admin输入密码123456点击登录'''
        self.login.input_user("admin")
        self.login.input_psw("123456")
        self.login.click_login_button()
        result = self.login.get_login_name()
        self.assertTrue(result =="admin")


    def test_02(self):
        '''输入账号admin不输入密码点击登录'''
        self.login.input_user("admin")

        self.login.click_login_button()
        result = self.login.get_login_name()
        self.assertTrue(result == "")

    def test_03(self):
        '''输入账号admin输入密码123456点击记住登录'''
        self.login.input_user("admin")
        self.login.input_psw("123456")
        self.login.click_keep_login()
        self.login.click_login_button()
        result = self.login.get_login_name()
        self.assertTrue(result == "admin")


    def test_04(self):
        '''忘记密码'''

        self.login.click_forget_psw()
        result = self.login.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main()