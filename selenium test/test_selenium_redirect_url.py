import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def test_blog_url_():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    assert "ZeRong's blog" == driver.title
    
    driver.close()


def test_project_url_():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/projects/")
    assert "ZeRong's Project" == driver.title
    
    driver.close()



def test_blog_CCA():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    assert 'blog comment' == driver.title
    
    driver.close()



def test_project_aboutme_url_():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/projects/5/")
    assert 'project details' == driver.title
    
    driver.close()




def test_admin_login_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("localhost:8000/admin/login/?next=/admin/")
    assert  'Log in | Django site admin' == driver.title
    
    driver.close()


