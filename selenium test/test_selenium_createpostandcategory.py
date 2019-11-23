import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def test_create_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/category/add/' and text()='Add']").click()
    driver.find_element_by_name("name").send_keys("Weekend Activity")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select category to change | Django site admin' == driver.title 
    driver.close()



def test_create_category_no_input_name():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/category/add/' and text()='Add']").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    errornote = driver.find_element_by_xpath("//*[contains(text(), 'Please correct the error below.')]").text
    assert  'Add category | Django site admin' == driver.title and "Please correct the error below." == errornote
    driver.close()


def test_create_post_without_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/post/add/' and text()='Add']").click()
    time.sleep(3)
    driver.find_element_by_name("title").send_keys("Weekdays activity")
    driver.find_element_by_name("body").send_keys("Monday - watch movies, Tuesday - have fun, Wednesday - working")   
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    errornote = driver.find_element_by_xpath("//*[contains(text(), 'Please correct the error below.')]").text
    errornoteCategory = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert  'Add post | Django site admin' == driver.title and 'Please correct the error below.'== errornote and 'This field is required.' == errornoteCategory
    driver.close()



def test_create_post_without_title():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/post/add/' and text()='Add']").click()
    time.sleep(2)
    driver.find_element_by_name("body").send_keys("Monday - watch movies, Tuesday - have fun, Wednesday - working")
    driver.find_element_by_xpath("//select[@name='categories']/option[text()='Category object (6)']").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    errornote = driver.find_element_by_xpath("//*[contains(text(), 'Please correct the error below.')]").text
    errornoteTitle = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert  'Add post | Django site admin' == driver.title and 'Please correct the error below.'== errornote and 'This field is required.' == errornoteTitle
    driver.close()



def test_create_post_without_title_and_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/post/add/' and text()='Add']").click()
    time.sleep(2)
    driver.find_element_by_name("body").send_keys("Monday - watch movies, Tuesday - have fun, Wednesday - working")   
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    errornote = driver.find_element_by_xpath("//*[contains(text(), 'Please correct the errors below.')]").text
    errornoteTitleandCategory = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert  'Add post | Django site admin' == driver.title and 'Please correct the errors below.'== errornote and 'This field is required.' == errornoteTitleandCategory
    driver.close()



def test_create_post_without_body():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/post/add/' and text()='Add']").click()
    time.sleep(2)
    driver.find_element_by_name("title").send_keys("Weekdays activity")
    driver.find_element_by_xpath("//select[@name='categories']/option[text()='Category object (6)']").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    errornote = driver.find_element_by_xpath("//*[contains(text(), 'Please correct the error below.')]").text
    errornoteBody = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert  'Add post | Django site admin' == driver.title and 'Please correct the error below.'== errornote and 'This field is required.' == errornoteBody
    driver.close()



def test_create_post_without_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/post/add/' and text()='Add']").click()
    time.sleep(2)
    driver.find_element_by_name("title").send_keys("Weekdays activity")
    driver.find_element_by_name("body").send_keys("Monday - watch movies, Tuesday - have fun, Wednesday - working")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    errornote = driver.find_element_by_xpath("//*[contains(text(), 'Please correct the error below.')]").text
    errornoteCategory = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert  'Add post | Django site admin' == driver.title and 'Please correct the error below.'== errornote and 'This field is required.' == errornoteCategory
    driver.close()

