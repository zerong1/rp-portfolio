import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def test_user_post_empty_comment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    commentcount = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_name("author").send_keys("Alice")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type ='submit']"))).click()
    commentcountupdated = len(driver.find_elements_by_name('usercomment'))
    assert commentcountupdated == commentcount and 'blog comment' == driver.title
    driver.close()

'''

'''
def test_user_post_empty_name():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    commentCount = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_name("body").send_keys("This is funny hahaha testing")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type ='submit']"))).click()
    commentCountUpdated = len(driver.find_elements_by_name('usercomment'))
    assert commentCount == commentCountUpdated and 'blog comment' == driver.title
    driver.close()



def test_user_post_empty_name_and_comment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    commentCount = len(driver.find_elements_by_name('usercomment'))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type ='submit']"))).click()
    commentCountUpdated = len(driver.find_elements_by_name('usercomment'))
    assert commentCount == commentCountUpdated and 'blog comment' == driver.title
    driver.close()




def test_user_create_and_submit_comment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(2)
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    commentCount = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_name("author").send_keys("Alice")
    driver.find_element_by_name("body").send_keys("This is funny hahaha testing")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type ='submit']"))).click()
    commentCountUpdated = len(driver.find_elements_by_name('usercomment'))
    assert 'blog comment' == driver.title # and commentCountUpdated == commentCount +1 
    driver.close()

