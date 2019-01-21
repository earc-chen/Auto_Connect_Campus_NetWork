# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:34:26 2019

@author: Yike
"""
from selenium import webdriver
import requests
import time

class Login:
    def __init__(self):
        self.url = 'your_campus_network_login_url'
        self.username = "your_username"
        self.password = "your_password"
   
    #判断当前是否可以连网
    def is_connect_web(self):
        try:
            status = requests.get("https://www.baidu.com")
            if(status.status_code == requests.codes.ok):
                return True
            else:
                return False
        except:
	    return False
            print ('error')
            
    def login(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        browser.implicitly_wait(10)
        user=browser.find_element_by_id("username")
        user.send_keys(self.username)
	#由于本校园网网站输入密码的文本框被隐藏了，需要先点击并列的上方文本框才能进行输入
	browser.find_element_by_xpath('//*[@id="pwd_tip"]').click()
	pwd=browser.find_element_by_xpath('//*[@id="pwd"]')
        pwd.send_keys(self.password)
	#先点击下拉按钮，然后再点击自己想下拉的那个运营商
	browser.find_element_by_id("xiala").click()
	service=browser.find_element_by_id("bch_service_1")
	service.click()
        submit=browser.find_element_by_xpath('//*[@id="loginLink_div"]')
        submit.click()
	#登录成功之后就可以关闭浏览器了
        browser.close()
login = Login()
n=1
#五秒钟检测是否能联网，如果不能联网，就需要进行重新登录校园网
while True:
	if login.is_connect_web():
		time.sleep(5)
	else:
		login.login()
		print '重连第'+str(n)+'次'	
		n=n+1