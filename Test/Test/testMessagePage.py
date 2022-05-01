from Test.BaseTest.base import *
from Utilts.utils import insert_data_to_form


phone= "0506040732"
fullName= "Israel Israeli"
message="hello"
def test_send_message_correctly():
    driver = init()
    # Go to massage page:
    driver.find_element(By.XPATH, "//a[contains(text(),'Messages')]").click()
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
    l = [phone,fullName, message]
    details = driver.find_elements(By.XPATH, "//form/child::*")

    insert_data_to_form(details,l)
    sleep(2)




















