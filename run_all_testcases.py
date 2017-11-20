#! /usr/bin/env python
# -*- coding:UTF-8 -*-


import unittest
from public.HTMLTestReportCN import HTMLTestRunner
import time

test_case_dir = '\\testcases'


def create_suite():
    test_suits = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(
        test_case_dir,
        pattern='test*',
        top_level_dir=None
    )

    for test_suit in discover:
        for test_case in test_suit:
            test_suits.addTest(test_case)
            print(test_suits)

    return test_suits

all_test_cases = create_suite()

now = time.strftime('%Y-%m_%d-%H_%M_%S', time.localtime())

file_name = '\\report\\' + now + 'result.html'

with open(file_name, 'wb') as fp:
    runner = HTMLTestRunner(
        stream=fp,
        title=u'web自动化测试报告',
        description=u'用例具体执行情况如下：'
    )

runner.run(all_test_cases)
