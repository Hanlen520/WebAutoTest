#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 'http://114.55.53.189:9094'
url = 'http://121.199.34.238:2000'
username = 'alex'
password = 'pcj6105859'


def login(driver, url=url, username=username, password=password):
    """登录"""
    driver.get(url)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_class_name('btn-submit').submit()


def logout(driver):
    driver.find_element_by_class_name('hidden-xs').click()
    # driver.find_element_by_class_name('btn btn-default btn-flat').click()
    driver.find_elements_by_css_selector('div.pull-left>a')[2].click()
    driver.quit()


if __name__ == "__main__":
    from selenium import webdriver
    import time
    for i in range(2):
        driver = webdriver.Chrome()
        url = 'http://114.55.53.189:9094'
        login(driver, url, 'alex', 'pcj6105859')
        time.sleep(2)
        logout(driver)

