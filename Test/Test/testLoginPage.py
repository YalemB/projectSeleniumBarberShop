from Test.BaseTest.base import *
from Utilts.utils import *

def init_without_login():
    driver = webdriver.Chrome('../../Driver/chromedriver.exe')
    driver.get("https://wondemagen-barbershop.herokuapp.com/")
    driver.maximize_window()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Login')]"))).click()
    return driver
#
email = "tsiona@gmail.com"
password = "123456"

#1
def test_login_correctly():
    driver = init_without_login()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH, "//form[1]/input[1]").send_keys(email)
    driver.find_element(By.XPATH, "//form[1]/input[2]").send_keys(password)
    driver.find_element(By.XPATH, "//form[1]/input[3]").click()
    value = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'log out')]"))).get_attribute("innerText")
    assert value == "log out"

#2
def test_invalid_login_when_password_incorrect():
    driver = init_without_login()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH, "//form[1]/input[1]").send_keys(email)
    driver.find_element(By.XPATH, "//form[1]/input[2]").send_keys("123")
    driver.find_element(By.XPATH, "//form[1]/input[3]").click()
    value = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//h4[contains(text(),'incorrect Password/Email')]"))).get_attribute("innerText")
    print(value)
    assert value == "incorrect Password/Email"

#3
def test_invalid_login_when_passwordField_is_null():
    driver = init_without_login()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH, "//form[1]/input[1]").send_keys(email)
    driver.find_element(By.XPATH, "//form[1]/input[2]").send_keys("")
    driver.find_element(By.XPATH, "//form[1]/input[3]").click()
    button = driver.find_element(By.XPATH,"//div[1]/form[1]/input[3]").is_enabled()
    assert button == False

#4
def test_invalid_login_when_emailField_is_null():
    driver = init_without_login()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH, "//form[1]/input[1]").send_keys("")
    driver.find_element(By.XPATH, "//form[1]/input[2]").send_keys(password)
    driver.find_element(By.XPATH, "//form[1]/input[3]").click()
    button = driver.find_element(By.XPATH,"//div[1]/form[1]/input[3]").is_enabled()
    assert button == False

#5
def test_invalid_login_when_all_fields_are_null():
    driver = init_without_login()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH, "//form[1]/input[1]").send_keys("")
    driver.find_element(By.XPATH, "//form[1]/input[2]").send_keys("")
    driver.find_element(By.XPATH, "//form[1]/input[3]").click()
    button = driver.find_element(By.XPATH, "//div[1]/form[1]/input[3]").is_enabled()
    assert button == False
