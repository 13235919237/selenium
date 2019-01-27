from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class Base():

    def __init__(self, driver:webdriver.Firefox): #:webdriver.Firefox映射到这个类
        self.driver=driver
        self.timeout=10
        self.t=0.5

    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回")
            return ""

    def get_attribute(self, locator,name):
        '''获取属性'''
        try:
            element=self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回"%name)
            return ""

    def findElement(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele

    def findElementNew(self, locator):
        '''定位到元素，返回元素对象，没定位到 返回Timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele

    def findElements(self, locator):
        try:
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []

    def is_title(self , _title):
        '''返回bool'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self , _title):
        '''返回bool'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self ,locator, _text):
        '''返回bool'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self ,locator , _value):
        '''返回bool value为空返回空字符串 返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        '''是否弹窗'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())

            return result
        except:
            return False

    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)


    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

       #判断有没有被选中
    def isSelected(self, locator):
        ele = self.findElement(locator)
        r=ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
          ele = self.findElement(locator)
          return True

        except:

          return False


    def isElementExist2(self, locator):
        eles = self.findElement(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n ==1:
            return True
        else:
            print("定位到元素的个数%s"%n)
            return True
    def move_to_element(self, locator):
        '''鼠标悬停事件  百度 鼠标悬停设置会出现选项 '''
        ele= self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()
    def select_by_index(self, locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认第一个'''
        element =self.findElement(locator)#定位到select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator,value):
        '''通过value属性'''
        element =self.findElement(locator)#定位到select这一栏
        Select(element).select_by_value(value)

    def select_by_text(self, locator,text):
        '''通过文本值定位'''
        element =self.findElement(locator)#定位到select这一栏
        Select(element).select_by_visible_text(text)

    def js_focus_element(self, locator):
        '''聚焦到元素 通常多定位一点避免广告'''
        target =self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

if __name__ == "__main__":
    driver = webdriver.Firefox();
    driver.get("http://127.0.0.1:8181/zentao/user-login-L3plbnRhby8=.html")
    zentao=Base(driver)
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")  #调用css xpath By.XPATH   By.CSS_SELECTOR

    zentao.sendKeys(loc1, "admin")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)
    #想要切换jframe可以这样，二次包装不影响其他  driver.switch_to.frame()

    # zentao.findElement(loc1).send_keys("admin")
    # zentao.findElement(loc2).send_keys("123456")
    # zentao.findElement(loc3).click()


