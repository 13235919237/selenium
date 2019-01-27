from selenium import webdriver
import  time
import unittest
class LoginTest(unittest.TestCase):
    ''' 登陆测试用例'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox();#加载火狐只执行一次
    def setUp(self):
        self.driver.get("http://127.0.0.1:8181/zentao/user-login-L3plbnRhby8=.html")
        self.is_alert_exists()
        self.driver.delete_all_cookies()
        self.driver.refresh()
    def get_login_username(self):
        try:
            t = self.driver.find_element_by_class_name('user-name').text
            print(t)
            return t
        except:
            return ""
    def is_alert_exists(self):
        try:
            alert=self.driver.switch_to.alert
            text=alert.text
            alert.accept()
            return text
        except:
            return ""

    def test_01(self):
        '''第一个测试'''
        time.sleep(2)
        self.driver.find_element_by_id('account').send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_css_selector("#keepLoginon").click()
        self.driver.find_element_by_css_selector('#submit').click()
        time.sleep(3)
        t=self.get_login_username()
        print("获取的结果是%s"%t)
        self.assertTrue(t=="admin")
    def test_02(self):
        '''第二个测试'''
        time.sleep(2)
        self.driver.find_element_by_id('account').send_keys("admin11")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_css_selector("#keepLoginon").click()
        self.driver.find_element_by_css_selector('#submit').click()
        time.sleep(3)
        t = self.get_login_username()
        print("登录失败，获取的结果是%s" % t)
        # self.assertTrue(t == "")
        self.assertTrue(1==2)#故意写错
    # def tearDown(self):
        # self.is_alert_exists()
        # self.driver.delete_all_cookies()
        # self.driver.refresh()
    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()



