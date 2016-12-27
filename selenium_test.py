#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-12-26 18:02:53

from selenium import webdriver

browser = webdriver.Chrome(service_args=['--ignore-ssl-errors=true'])
browser.get("https://mail.inmindglobal.com")
user_element = browser.find_element_by_id('username')
user_element.send_keys('huangyr@inmindglobal.com')
password_element = browser.find_element_by_id("password")
password_element.send_keys('Inmind888')
login_btn = browser.find_element_by_class_name('signinTxt')
login_btn.click()
menu_btn = browser.find_element_by_class_name('o365cs-navMenuButton')
menu_btn.click()
calendar_btn = browser.find_element_by_class_name('ms-Icon--calendar')
calendar_btn.click()
new_calendar = browser.find_element_by_id('_ariaId_152')
new_calendar_head = browser.find_elements_by_class_name('_fce_b')[1]
new_calendar_btn = new_calendar_head.find_elements_by_tag_name('button')[0]
new_calendar_btn.click()

new_item_form = browser.find_element_by_class_name('popupPanel')
lis = new_item_form.find_elements_by_tag_name('li')
title_input = lis[0].find_element_by_tag_name('input')
title_input.send_keys('标题')
