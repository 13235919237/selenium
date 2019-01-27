from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from common.base import Base
login_url="http://127.0.0.1:8181/zentao/user-login-L3plbnRhby8=.html"
class LoginPage(Base):
    #定位元素
    loc_user = ("id", "account")
    loc_psw = ("name", "password")
    loc_keep = ("id","keepLoginon")
    loc_button = ("id", "submit")
    loc_forget_psw=("link text","忘记密码")
    loc_get_user = ("class name","user-name")
    loc_forget_psw_page=("xpath","html/body/div[1]/div/div[2]/div[2]/a")
    def input_user(self,text=""):
        self.sendKeys(self.loc_user,text)

    def input_psw(self, text=""):
        self.sendKeys(self.loc_psw, text)


    def click_keep_login(self): #保存登录
        self.click(self.loc_keep)

    def click_login_button(self):  # 点击登录
        self.click(self.loc_button)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)


    def login(self, user="admin",psw="123456" ,keep_login=False):
        '''登录方法'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        #保持登录默认是关的，如果true就点击保持登录
        if keep_login : self.click_keep_login()
        self.click_login_button()

    def get_login_name(self):
        user = self.get_text(self.loc_get_user)
       # user = self.driver.find_element_by_class_name('user-name').text
        return user

    def get_login_result(self, user):
        '''是不是期望结果 是True'''
        result = self.is_text_in_element(self.loc_get_user ,user)
        return result


    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回")
            return ""

    def is_alert_exists(self):
        '''判断alert是不是在'''
    # try:
        a= self.is_alert()
        if a:
            print(a.text)
            a.accept()
            # alert = self.driver.switch_to.alert
            # text = alert.text
            # alert.accept()
            # return text
        # except:
        #     return False

    def is_refresh_exist(self):
        '''判断忘记密码页刷新是否存在'''
        r=self.isElementExist(self.loc_forget_psw_page)
        return  r



if __name__ == "__main__":
    driver=webdriver.Firefox()
    login_page=LoginPage(driver)#实例化
    login_page.login() #里面加上keep_login=True 就会点击保持登录
    # driver.get(login_url)#打开网址
    # login_page.input_user("admin")#对象。方法
    # login_page.input_psw("123456")
    # login_page.click_keep_login()
    # login_page.click_login_button()
