#! /usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import unittest


class Login(unittest.TestCase):

    def setUp(self):
        self.login_url = 'http://114.55.53.189:9094'
        self.logout_url = 'https://cas.thecover.cn/cas/logout'
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)

    def test_login_all_null(self):
        """账号密码为空"""
        self.driver.get(self.login_url)
        self.driver.find_element_by_class_name('btn-submit').submit()
        time.sleep(2)
        try:
            username = self.driver.find_element_by_class_name('hidden-xs').text
        except Exception as e:
            username = e.msg
            print(username)
        self.assertEqual('Alex', username)

    def test_login_success(self):
        """账号密码正确，登录成功"""
        self.driver.get(self.login_url)
        self.driver.find_element_by_id('username').send_keys('alex')
        self.driver.find_element_by_id('password').send_keys('pcj6105859')
        self.driver.find_element_by_class_name('btn-submit').submit()
        time.sleep(2)
        username = self.driver.find_element_by_class_name('hidden-xs').text
        self.assertEqual('Alex', username)

    def test_logout(self):
        pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()