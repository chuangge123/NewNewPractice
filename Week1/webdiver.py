# -*-coding = utf-8-*-
# __author:"NGLS Chuang"
# @time:2019/12/10 17:20
import time
import unittest
import re
import time
import os
from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LagouSpider(object):
    driver_path = r"C:\PyCharm\workspace\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "http://10.11.24.129:8080/"
        self.positions = []

    def run(self):
        # 登录行为链
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="userLayout"]/div/div[2]/i').click()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('23070619960711061X')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # time.sleep(3)
        # 等待研讨元素，并进入研讨
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li[2]/a'))
        )
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        # 点击联系人并进入院机关，进入国际合作部，发送消息行为链接
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/span/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[3]/div[2]/ul/li[1]/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[3]/div[2]/ul/li[1]/ul/li[14]/span[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[3]/div[2]/ul/li[1]/ul/li[14]/ul/li[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[3]/div/div[2]/button').click()
        time.sleep(0.5)
        # for i in range(99):
        #     self.driver.find_element_by_xpath(
        #         '//*[@id="app"]/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div/textarea').send_keys('face[玫瑰]',)
        #     self.driver.find_element_by_xpath(
        #         '//*[@id="app"]/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[3]/div/button').click()
        # 传文件按钮。
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[1]/div[2]/i').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/ul/li/div/span/div/span/span').click()
        time.sleep(0.5)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/i[1]/svg').click()
        # self.driver.find_element_by_xpath()
        os.system(r"C:\Users\lark\Pictures\Camera Roll\test.jpg")
#         提交分支。
        time.sleep(1)

if __name__ == '__main__':
    a = LagouSpider()
    a.run()
