import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def test_maintain_user_list():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/' and text()='Change']").click()
    assert  'Select user to change | Django site admin' == driver.title

    driver.close()



def test_view_admin_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/' and text()='Change']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='/admin/auth/user/2/change/'and text()='alice']").click()
    usernametxtbox = driver.find_element_by_name("username").get_attribute('value')
    assert  'Change user | Django site admin' == driver.title and 'http://localhost:8000/admin/auth/user/2/change/' == driver.current_url
    driver.close()

