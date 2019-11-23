import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_superuser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    assert  'Site administration | Django site admin' == driver.title
    
    driver.close()




def test_admin_login_fakeuseraccount():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("fakeid")
    driver.find_element_by_name("password").send_keys("fakepassword")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    error_note = driver.find_element_by_class_name("errornote").text
    assert 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.'== error_note and 'Log in | Django site admin' == driver.title
    
    driver.close()



def test_admin_login_no_username_input():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("password").send_keys("fakepassword")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    assert 'Log in | Django site admin' == driver.title
    
    driver.close()



def test_admin_login_no_username_and_password_input():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    assert 'Log in | Django site admin' == driver.title
    
    driver.close()

