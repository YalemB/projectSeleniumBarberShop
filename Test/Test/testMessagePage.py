from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utils.utils import insert_data_to_form

#my user :
email = "tsiona@gmail.com"
password = "123456"

def init():
    email = "tsiona@gmail.com"
    password = "123456"
    driver = webdriver.Chrome('..\Driver\chromedriver.exe')
    driver.get("https://wondemagen-barbershop.herokuapp.com/")
    driver.maximize_window()
    #Login with email and password :
    driver.find_element(By.XPATH,"//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH,"//form[1]/input[1]").send_keys(email)
    sleep(2)
    driver.find_element(By.XPATH,"//form[1]/input[2]").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH,"//form[1]/input[3]").click()
    sleep(2)
    #Go to massage page:
    driver.find_element(By.XPATH,"//a[contains(text(),'Messages')]").click()
    return driver


phone= "0506040732"
fullName= "Israel Israeli"
message="hello"
def test_send_message_correctly():
    driver = init()
    l=[phone,fullName,message]
    details = driver.find_elements(By.XPATH,"//form/child::*")
    x = 0
    for i in details:
        if i.tag_name == "input" or i.tag_name == "textarea":
            if x < 3 :
                i.send_keys(l[x])
                x += 1
            else:
                i.click()
    sleep(3)

def test_send_message_incorrectly_whenPhoneFieldNull():
    driver = init()
    l=["",fullName,message]
    details = driver.find_elements(By.XPATH,"//form/child::*")
    x = 0
    for i in details:
        if i.tag_name == "input" or i.tag_name == "textarea":
            if x < 3 :
                i.send_keys(l[x])
                x += 1
            else:
                i.click()
    sleep(3)


def test_send_message_incorrectly_whenNameFieldNull():
    driver = init()
    l=[phone,"",message]
    details = driver.find_elements(By.XPATH,"//form/child::*")
    x = 0
    for i in details:
        if i.tag_name == "input" or i.tag_name == "textarea":
            if x < 3 :
                i.send_keys(l[x])
                x += 1
            else:
                i.click()
    sleep(3)

def test_ghgg():
    driver = init()
    l = [phone, "", message]
    details = driver.find_elements(By.XPATH, "//form/child::*")

    insert_data_to_form(details,l)
    sleep(2)




















