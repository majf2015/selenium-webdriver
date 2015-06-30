# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Shidou(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.shidou.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_shidou(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_css_selector("a.banner1_circle").click()
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_id("slider1-next").click()
        driver.find_element_by_id("slider1-next").click()
        driver.find_element_by_id("slider1-next").click()
        driver.find_element_by_id("slider1-next").click()
        driver.find_element_by_link_text(u"石豆新闻").click()
        driver.find_element_by_link_text(u"点击查看").click()
        driver.find_element_by_link_text(u"\"连接伙伴，共享未来\"中新石豆亮相第十一届文博会博得喝彩").click()
        driver.back()
        driver.find_element_by_link_text(u"石豆参与佛山市公共场所3万个免费WiFi建设工作——以\"三高准则\"为广大市民提供安全、高效的网络服务").click()
        driver.back()
        driver.find_element_by_xpath(u"(//a[contains(text(),'合作加盟')])[2]").click()
        driver.find_element_by_link_text(u"产品咨询").click()
        driver.find_element_by_link_text(u"关于石豆").click()
        driver.find_element_by_link_text(u"石豆名称的由来").click()
        driver.find_element_by_link_text(u"产品服务").click()
        driver.find_element_by_css_selector("#slider3-nav > li.act").click()
        driver.find_element_by_id("slider3-next").click()
        driver.find_element_by_id("slider3-next").click()
        driver.find_element_by_id("slider3-next").click()
        driver.find_element_by_id("slider3-next").click()
        driver.find_element_by_id("slider3-next").click()
        driver.find_element_by_id("slider3-next").click()
        driver.find_element_by_id("slider3-p3").click()
        driver.find_element_by_link_text("93WiFi").click()
        driver.find_element_by_link_text(u"石豆网关").click()
        driver.find_element_by_link_text(u"石豆营销系统").click()
        driver.find_element_by_link_text(u"产品案例").click()
        driver.find_element_by_css_selector("dt.casv-nav2").click()
        driver.find_element_by_css_selector("dt.casv-nav3").click()
        driver.find_element_by_css_selector("dt.casv-nav4").click()
        driver.find_element_by_css_selector("dt.casv-nav1").click()
        driver.find_element_by_link_text(u"合作加盟").click()
        driver.find_element_by_css_selector("div.left.ianimate").click()
        driver.find_element_by_id("info-company").clear()
        driver.find_element_by_id("info-company").send_keys(u"自动化测试")
        driver.find_element_by_id("info-username").clear()
        driver.find_element_by_id("info-username").send_keys(u"自动化测试")
        driver.find_element_by_id("info-tel").clear()
        driver.find_element_by_id("info-tel").send_keys("13454545429")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text(u"合作加盟").click()
        driver.find_element_by_link_text(u"联系我们").click()
        driver.find_element_by_id("info-name").clear()
        driver.find_element_by_id("info-name").send_keys(u"自动化测试")
        driver.find_element_by_id("info-email").clear()
        driver.find_element_by_id("info-email").send_keys("10210085@qq.com")
        driver.find_element_by_id("info-question").clear()
        driver.find_element_by_id("info-question").send_keys(u"尽量做成自动化测试")
        driver.find_element_by_id("about-submit").click()
        driver.find_element_by_link_text(u"人才招聘").click()
        driver.find_element_by_link_text(u"java后台开发工程师").click()
        driver.find_element_by_link_text(u"销售代表").click()
        driver.find_element_by_link_text(u"web前端开发工程师").click()
        driver.find_element_by_link_text(u"java后台开发工程师").click()
        driver.find_element_by_link_text(u"销售代表").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
