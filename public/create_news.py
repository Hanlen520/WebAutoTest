#! /usr/bin/env python
# -*- coding:UTF-8 -*-
import time


class ManageNews():

    def __init__(self):
        pass

    def create_news(self, channel, label_type, title, content, source, pct_list):
        """
        :param channel：频道名称
        :param label_type: 变迁类型。0：无， 1：广告， 2：活动， 3：纯外链， 4：精选， 5：独家
        :param title: 文章标题
        :param content: 文章内容
        :param source: 新闻来源
        :param pct_list: 正文上传的图片列表
        :return: None表示成功，否则表示有异常
        """
        # 点击编辑发布库
        self.driver.find_element_by_xpath(".//*[@id='body']/div[1]/aside/div/section/ul/ul/li[2]/a").click()
        time.sleep(2)
        ll = self.driver.find_elements_by_xpath(".//*[@id='body']/div[1]/aside/div/section/ul/ul/li[2]/ul/li")
        for i in ll:
            if i.text == channel:
                i.click()
        time.sleep(2)
        # 点击发布文章
        self.driver.find_element_by_css_selector('div.box-body>div.btn-group>button').click()
        # 获取当前窗口句柄
        now_handle = self.driver.current_window_handle
        time.sleep(3)
        label_list = self.driver.find_elements_by_css_selector('div.modal-content>div>button')
        for label in label_list:
            if label.text == label_type:
                label.click()
        # self.driver.find_elements_by_css_selector('div.modal-content>div>button')[0].click()
        time.sleep(5)
        # 获取所有窗口句柄
        all_handle = self.driver.window_handles
        for handle in all_handle:
            if handle != now_handle:
                self.driver.switch_to_window(handle)
                time.sleep(2)
                self.driver.find_element_by_id('title').send_keys(title)
                self.driver.find_element_by_id('titleList').click()
                time.sleep(1)

                # 步骤一，先加入内容
                self.driver.switch_to_frame('ueditor_0')
                self.driver.find_elements_by_xpath(".//*[@id='edui3_body']/div")
                content = "alex测试文章内容。。啦啦"
                self.driver.find_element_by_css_selector('body.view>p').click()
                self.driver.find_element_by_css_selector('body.view').send_keys(content)
                # time.sleep(6)
                # 不知道啥原因这种方式没法输入，调试的时候可以
                # self.driver.find_element_by_class_name('view').send_keys(content)
                time.sleep(2)
                self.driver.switch_to.default_content()

                # 步骤二，添加图片

                # 点击批量选择图片
                self.driver.find_elements_by_css_selector('div#edui65')[0].click()
                # 切换到图片选择框
                self.driver.switch_to_frame('edui61_iframe')
                # 选择图片
                self.driver.find_element_by_name('file').send_keys("C:\\Alex\\1564646.jpg")
                # 上传七牛云
                self.driver.find_element_by_class_name('uploadBtn').click()
                time.sleep(2)
                self.driver.switch_to.default_content()
                # 点击确认，关闭弹窗
                self.driver.find_elements_by_xpath(".//*[@id='edui63_body']/div[2]")[0].click()

                time.sleep(1)
                self.driver.find_element_by_css_selector('input#sourceStr').send_keys("新华网")
                time.sleep(1)

                # 选择无图
                # self.driver.find_elements_by_css_selector('div.ant-col-24>div>label>span.ant-radio')[0].click()

                # 选择有图，从正文添加图片
                self.driver.find_elements_by_css_selector('div.ue-btn-group')[3].find_elements_by_tag_name('span')[
                    0].click()
                # 选中图片
                self.driver.find_elements_by_css_selector('div.content-select-img>ul>li>img')[0].click()
                # 点击确定
                self.driver.find_elements_by_class_name('ant-confirm-btns')[0].find_elements_by_tag_name('button')[
                    1].click()
                time.sleep(2)
                # 确定裁剪
                self.driver.find_elements_by_class_name('ant-confirm-btns')[0].find_elements_by_tag_name('button')[
                    1].click()
                time.sleep(3)
                # 选择一键裁图
                self.driver.find_elements_by_css_selector('div.ue-btn-group')[3].find_elements_by_tag_name('span')[
                    1].click()

                time.sleep(1)
                self.driver.find_elements_by_css_selector("div.ant-row>div.ant-col-3>button")[0].click()