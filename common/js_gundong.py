from selenium import webdriver
import time
from WebZidong2.common.base import Base
driver = webdriver.Firefox()
#driver.get("https://www.cnblogs.com/yoyoketang/")
driver.get("http://sh.ganji.com")
time.sleep(3)
# #滚动底部
# def gundon():
#
#     js = "window.scrollTo(0, document.body.scrollHeight)"
#     driver.execute_script(js)
#     time.sleep(3)
#     #划上来
#     js = "window.scrollTo(0,0)"
#     driver.execute_script(js)

#滚动到元素出现的位置 向定位到二手车 避免被广告挡住 多定位上面一点
# ele = driver.find_element_by_link_text("写字楼出售")
# driver.execute_script("arguments[0].scrollIntoView();", ele)
shili =Base(driver)
loc1=("link text","写字楼出售")
shili.js_focus_element(loc1)