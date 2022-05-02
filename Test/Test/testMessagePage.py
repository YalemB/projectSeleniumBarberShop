from Test.BaseTest.base import *
from Utilts.utils import *

phone= "0506040732"
fullName= "Israel Israeli"
message="hello"
pageMessage ="//a[contains(text(),'Messages')]"

#1
def test_send_message_correctly():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, pageMessage ))).click()
    data_fields = [phone, fullName , message]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = True

    test_send_message_button(form_element, data_fields, expected_is_enabled)
    form_element[-1].click()

#2
def test_send_message_incorrectly_whenPhoneFieldNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, pageMessage ))).click()
    data_fields = ["", fullName , message]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields, expected_is_enabled)

#3
def test_send_message_incorrectly_whenNameFieldNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = [phone, "", message]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields, expected_is_enabled)
    sleep(3)

#4
def test_send_message_incorrectly_whenMessageFieldNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = [phone, fullName, ""]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields, expected_is_enabled)
    sleep(3)
#5
def test_send_message_incorrectly_whenPhoneAndNameFieldsAreNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = ["", "",message]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields , expected_is_enabled)
    sleep(3)

#6
def test_send_message_incorrectly_whenNameAndMessageFieldAreNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = [phone, "", ""]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields , expected_is_enabled)
    sleep(3)

#7
def test_send_message_incorrectly_whenPhoneAndMessageFieldAreNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = ["" , fullName, ""]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields , expected_is_enabled)
    sleep(3)

#8
def test_send_message_incorrectly_whenAllFieldsAreNull():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = ["" , "" , ""]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields , expected_is_enabled)
    sleep(3)

#9
def test_send_message_incorrectly_byLessThan10DigitsInPhoneField():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, pageMessage ))).click()
    data_fields = ["0526", fullName , message]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields, expected_is_enabled)

#10
def test_send_message_incorrectly_whenNameFieldsIsWithNumbers():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    data_fields = [phone, "1234", message]
    form_element = driver.find_elements(By.XPATH, "//form/child::*")
    expected_is_enabled = False

    test_send_message_button(form_element, data_fields, expected_is_enabled)
    sleep(3)


#UI Test:
#1
def test_UI_navbar():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    nav = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]").get_attribute("innerText")
    assert nav == "Home Staff Products Gallery Review Messages"

#2
def test_UI_log_out_button():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    logOut = driver.find_element(By.XPATH, "//button[contains(text(),'log out')]").get_attribute("innerText")
    assert logOut == "log out"

#3
def test_UI_title():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    title = driver.find_element(By.XPATH, "//span[contains(text(),'wondemagen barbershop')]").get_attribute("innerText")
    assert title == "wondemagen barbershop"

#4
def test_UI_form_title():
    driver = init()
    # Go to massage page:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pageMessage))).click()
    formTitle = driver.find_element(By.XPATH, "//h4[contains(text(),'User Messages')]").get_attribute("innerText")
    assert formTitle == "User Messages"
