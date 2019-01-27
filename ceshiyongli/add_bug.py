from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from common.base import Base
class ZenTaoBug(Base):
    #定位元素
    loc1 = ("id", "account")
    loc2 = ("name", "password")
    loc3 = ("id", "submit")
    #添加BUG
    loc_test = ("link text", "测试")
    loc_bug = ("xpath",".//*[@id='subNavbar']/ul/li[1]/a")
    loc_addbug = ("xpath",".//*[@id='mainMenu']/div[3]/a[3]")
    loc_truck = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_truck_add =("xpath",".//*[@id='openedBuild_chosen']/div/ul/li[1]")
    loc_input_title =("id", "title")
    #需要先切换
    loc_input_body = ("class name", "article-content")
    loc_avse = ("css selector","#submit")
    #新增的列表（标题）提bug成功后判断有没有在
    loc_new =("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[3]/a")
    def login(self, user="admin",psw="123456"):
        self.driver.get("http://127.0.0.1:8181/zentao/user-login-L3plbnRhby8=.html")
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,psw)
        self.click(self.loc3)
    def add_bug(self, title="测试提交BUG"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)
        #self.sendKeys(self.loc_input_title,"测试标题")
        self.sendKeys(self.loc_input_title, title)
        #输入标题
        frame=self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        #富文本不能clear
        body ='''[测试步骤]xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()
        self.click(self.loc_avse)
    def is_add_bug_sucess(self,_text):

        return self.is_text_in_element(self.loc_new, _text)
if __name__ =="__main__":
    driver = webdriver.Firefox()
    bug = ZenTaoBug(driver)
    bug.login()
    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试提交BUG"+timestr
    bug.add_bug(title)
    result = bug.is_add_bug_sucess(title)
    print(result)



