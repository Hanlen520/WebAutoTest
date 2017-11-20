#! /usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.vmall.com')
# driver.find_element_by_class_name('product-button02').click()
# driver.find_element_by_class_name('qqLogin_bigIco').click()
driver.find_element_by_id('top-index-loginUrl').click()
driver.find_element_by_class_name('qqLogin_bigIco').click()
# 如果html中有frame必须使用swich_to_frame不然无法定位元素
driver.switch_to_frame('ptlogin_iframe')
driver.find_element_by_id('nick_120279687').click()
count = 0
while True:
    try:
        print(count)
        time.sleep(0.5)
        driver.refresh()
        driver.find_element_by_class_name('product-button02').click()
        count += 1
    except Exception as e:
        count += 1
        print(e)
        driver.refresh()
        continue
time.sleep(52)
