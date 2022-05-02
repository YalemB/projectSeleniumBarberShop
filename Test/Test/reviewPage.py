from Utilts.utils import *
from Test.BaseTest.base import *

def test_leave_review_correctly_for_aviel():
    # review page button
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    data = ["aviel", "asi", "Nice barber"]
    expected_result = True

    page.click()
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    form[-1].click()

    driver.quit()



def test_validate_reivew_message_for_aviel():
    # review page button
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()

    validate = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,"//table[1]/tr[69]/td[3]"))
    ).text
    assert validate == "HOribbel barber"
    driver.quit()


def test_leave_review_correctly_for_osher():
    # review page button
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )


    data = ["osher", "yalem", "Good barber"]
    expected_result = True

    page.click()
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    form[-1].click()
    driver.quit()

def test_validate_reivew_message_for_osher():
    # review page button
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()

    validate = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,"//table[1]/tr[70]/td[3]"))
    ).text
    assert validate == "Good barber"
    driver.quit()


#the barber name is not aviel or osher
def test_leave_review_incorrectly_by_diff_barber():

    # review page button
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )


    page.click()
    data = ["mosha", "yalem", " Not Good barber"]
    form = driver.find_elements(By.XPATH, "//form/child::*")
    expected_result = False

    send_message_button(form,data,expected_result)
    driver.quit()

#barber name field null
def test_leave_review_incorrectly_by_null_barber_name():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()


    data = ["", "yalem", " Not Good barber"]

    form = driver.find_elements(By.XPATH, "//form/child::*")
    expected_result = False

    send_message_button(form,data,expected_result)
    driver.quit()

#barber name field null
def test_leave_review_incorrectly_by_null_full_name():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    data = ["aviel", "", " Not Good barber"]
    expected_result = False
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    driver.quit()

#message  field null
def test_leave_review_incorrectly_by_null_message_field():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    data = ["aviel", "yalem", ""]
    expected_result = False
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    driver.quit()


#only message field
def test_leave_review_incorrectly_by_only_message_field():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    data = ["", "", " Not Good barber"]
    expected_result = False
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    driver.quit()

#only barber name
def test_leave_review_incorrectly_by_only_barber_name():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    data = ["aviel", "", " "]
    expected_result = False
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    driver.quit()

#only fullname field
def test_leave_review_incorrectly_by_only_fullname():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    data = ["", "yalem", " "]
    expected_result = False
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    driver.quit()


#all  fields null
def test_leave_review_incorrectly_by_null_all_field():

    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    data = ["", "", ""]
    expected_result = False
    form = driver.find_elements(By.XPATH, "//form/child::*")

    send_message_button(form,data,expected_result)
    driver.quit()

def test_ui_babershop_sigh():
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    page.click()
    value = driver.find_element(By.XPATH,"//span[1]").get_attribute("innerText")
    assert value == "wondemagen barbershop"
    driver.quit()


def test_ui_form_title():
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    page.click()
    value = driver.find_element(By.XPATH,"//h4[1]").get_attribute("innerText")
    assert value == "User Reviews"
    driver.quit()

def test_ui_table_title():
    driver = init()
    review = "//*[@id='root']/div/div[1]/a[5]"
    page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, review))
    )

    page.click()
    value = driver.find_element(By.XPATH,"//table[1]/tr[1]").get_attribute("innerText")
    assert value == "full name	barber name	review"
    driver.quit()










