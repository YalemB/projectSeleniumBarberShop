from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def init():
    email = "tsiona@gmail.com"
    password = "123456"
    # driver = webdriver.Chrome('..\Driver\chromedriver.exe')
    driver = webdriver.Chrome('..\Driver\chromedriver.exe')
    driver.get("https://wondemagen-barbershop.herokuapp.com/")
    driver.maximize_window()
    #Login with email and password :
    driver.find_element(By.XPATH,"//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH,"//form[1]/input[1]").send_keys(email)
    driver.find_element(By.XPATH,"//form[1]/input[2]").send_keys(password)
    driver.find_element(By.XPATH,"//form[1]/input[3]").click()
    return driver
