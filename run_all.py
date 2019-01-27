import unittest
from WebZidong2.common import HTMLTestRunner_cn
#用例的路径
casePath = r"F:\软件测试前端实例\untitled\WebZidong2\ceshiyongli"
rule ="test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
reportPath=r"F:\软件测试前端实例\untitled\WebZidong2\ceshibaogao\\"+"result.html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                        title="报告的名称",
                                        description="描述你的报告干什么用的",
                                        retry=1)
runner.run(discover)
fp.close()

