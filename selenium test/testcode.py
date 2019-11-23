import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''

def test_admin_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("localhost:8000/admin/login/?next=/admin/")
    assert  'Log in | Django site admin' == driver.title
    
    driver.close()

'''
'''


def test_project_url_():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/projects/")
    assert 'Project' == driver.title
    
    driver.close()
'''

'''
def test_blog_url_():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    assert 'blog' == driver.title
    
    driver.close()
'''


'''
def test_blog_CCA():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    assert 'blog comment' == driver.title
    
    driver.close()
'''



'''
def test_user_create_and_submit_empty_comment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type ='submit']"))).click()
    #driver.find_element_by_name("author").send_keys("Alice")
    #driver.find_element_by_name("body").sendkeys("This is funny hahaha testing") 
    assert  'blog comment' == driver.title
    
    driver.close()

'''

'''
def test_suepruser_create_and_submit_comment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()   
    driver.find_element_by_name("author").send_keys("Alice")
    driver.find_element_by_name("body").send_keys("This is funny hahaha testing")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type ='submit']"))).click()
    assert  'blog comment' == driver.title
    
    driver.close()
'''


'''
def test_admin_login_superuser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    assert  'Site administration | Django site admin' == driver.title
    
    driver.close()

'''

'''
def test_admin_login_fakesuperuseraccount():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("fakeid")
    driver.find_element_by_name("password").send_keys("fakepassword")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    'Log in | Django site admin' == driver.title
    
    driver.close()
'''

'''
def test_admin_create_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/add/' and text()='Add']").click()
    driver.find_element_by_name("username").send_keys("ilovenphahaha")
    driver.find_element_by_name("password1").send_keys("sasukexXX")
    driver.find_element_by_name("password2").send_keys("sasukexXX")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select user to change | Django site admin' == driver.title
    
    driver.close()
'''

'''
def test_admin_create_user_nopassword():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@href ='/admin/auth/user/add/' and text()='Add']").click()
    driver.find_element_by_name('username').send_keys("iloveicthahaha")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
  
    assert  'Add user | Django site admin' == driver.title
    
    driver.close()
'''

'''
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
'''

'''
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
'''

'''
def test_create_category_noinput():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href ='/admin/blog/category/add/' and text()='Add']").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Add category | Django site admin' == driver.title
    driver.close()
'''

'''
def test_create_post_with_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("alice")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    driver.find_element_by_xpath("//a[@href ='/admin/blog/post/add/' and text()='Add']").click()
    time.sleep(3)
    driver.find_element_by_name("title").send_keys("Weekdays activity")
    driver.find_element_by_name("body").send_keys("Monday - watch movies, Tuesday - have fun, Wednesday - working")
    driver.find_element_by_xpath("//select[@name='categories']/option[text()='Category object (6)']").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()

    assert  'Select post to change | Django site admin' == driver.title
    driver.close()

'''

'''
def test_blog_CCA():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href ='/blog/3/' and text()='CCA Activities']").click()
    #title = driver.find_element_by_name("title")
    assert 'blog comment' == driver.title
    
    driver.close()
'''
