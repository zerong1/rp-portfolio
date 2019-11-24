import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def test_admin_create_user_sucess():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/admin/auth/user/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    row_count = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    driver.find_element_by_xpath("//a[@class='addlink']").click()
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("ilovenphahaha")
    driver.find_element_by_name("password1").send_keys("sasukexXX")
    driver.find_element_by_name("password2").send_keys("sasukexXX")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    row_count2 = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    assert row_count2 == row_count +1
    driver.close()


def test_admin_create_user_username__field_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/add/' and text()='Add']").click()
    driver.find_element_by_name("password1").send_keys("sasukexXX")
    driver.find_element_by_name("password2").send_keys("sasukexXX")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    error_note = driver.find_element_by_class_name("errornote").text
    error_note_username = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert "Please correct the error below." == error_note and 'This field is required.'== error_note_username  and "Add user | Django site admin" == driver.title
    
    driver.close()



def test_admin_create_user_password__field_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/add/' and text()='Add']").click()
    driver.find_element_by_name('username').send_keys("iloveicthahaha")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    error_note = driver.find_element_by_class_name("errornote").text
    error_note_password = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert "Please correct the errors below." == error_note and 'This field is required.'== error_note_password  and "Add user | Django site admin" == driver.title
    
    driver.close()
'''

'''
def test_admin_create_user_common_password_field():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/add/' and text()='Add']").click()
    driver.find_element_by_name('username').send_keys("iloveicthahaha")
    driver.find_element_by_name("password1").send_keys("password")
    driver.find_element_by_name("password2").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    error_note = driver.find_element_by_class_name("errornote").text
    error_note_password = driver.find_element_by_xpath("//*[contains(text(), 'This password is too common.')]").text
    assert "Please correct the error below." == error_note and 'This password is too common.'== error_note_password  and "Add user | Django site admin" == driver.title
    
    driver.close()



def test_admin_create_user_password_field_less_than_eight_chars():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/add/' and text()='Add']").click()
    driver.find_element_by_name('username').send_keys("iloveicthahaha")
    driver.find_element_by_name("password1").send_keys("1234567")
    driver.find_element_by_name("password2").send_keys("1234567")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    error_note = driver.find_element_by_class_name("errornote").text
    error_note_password = driver.find_element_by_xpath("//*[contains(text(), 'This password is too short. It must contain at least 8 characters.')]").text
    assert "Please correct the error below." == error_note and 'This password is too short. It must contain at least 8 characters.'== error_note_password  and "Add user | Django site admin" == driver.title
    
    driver.close()

