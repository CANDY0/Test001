from selenium import webdriver
import unittest,time
from public import login
import xml.dom.minidom

dom=xml.dom.minidom.parse('G:\\Python_Project1\\test_data\\login.xml')
root=dom.documentElement
logins = root.getElementsByTagName('')
logins = root.getElementsByTagName('correct')
username = logins[0].getAttribute("username")
password = logins[0].getAttribute("password")

class TestDelMail(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        logins=root.getElementsByTagName('url')
        self.base_url=logins[0].firstChild.data
        self.verificationErrors=[]

    def test_del_mail(self):
        driver=self.driver
        driver.get(self.base_url)
        login.login(self,username,password)
        #点击收件箱
        driver.find_element_by_class_name('nui-tree-item-text').click()
        time.sleep(2)
        #查找一组 class='nui-chk-symbol'的下面的 p 标签，也就是每一封邮件前面的复选框，通过 pop(1)找到这一组复选框的第一个进行勾选
        driver.find_elements_by_xpath("//span[@class='nui-chk-symbol']/b").pop(1).click()
        #通过一组 span 标签中找到 text 等于“删除”的元素，点击删除按钮
        try:
            spans = driver.find_elements_by_tag_name('span')
            for s in spans:
                if s.text == u'删 除':
                    s.click()
        except:
            pass
        text=driver.find_element_by_css_selector('span.nui-tips-text>a').text
        self.assertEqual(text,'已删除')
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    unittest.main()


