from Test.BaseTest.base import *

# init without login for registration tests.
def init_registration():
    driver = webdriver.Chrome('../../Driver/chromedriver.exe')
    driver.get("https://wondemagen-barbershop.herokuapp.com")
    return driver



# random numbers will be added, to the email string -> "random numbers"+"@mail.com"
def rd():
    b = ""
    while len(b) < 9:
        # create random numbers and join them as a string
        a = randint(0, 9)
        b = b + str(a)
    return b




# shortcuts to elements/butons in registeration section
register_page = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[2]"
enter_pass = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[1]"
enter_confirm_pass = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[2]"
enter_email = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[3]"
sign_up = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[4]"
logout_button = "//button[contains(text(),'log out')]"


# shortcuts to elements/butons in login section
login_button = "//button[contains(text(),'Login')]"
login_enter_mail = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[1]"
login_enter_pass = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[2]"
sign_in_button = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[3]"



# registration with valid information
def test_successful_registration():
    driver = init_registration()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123123")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123123")
    # email will be created with the rd() function
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify you registered and the logout button appear
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,logout_button))
    ).get_attribute("innerText")
    assert value == "log out"



# registration with valid email and unmatched passwords
def test_failed_registration_valid_email_unmatched_password():
    driver = init_registration()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123654")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123232")
    # email will be created with the rd() function
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"






def test_failed_registration_null_fields():
    driver = init_registration()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("")
    driver.find_element(By.XPATH,enter_email).send_keys("")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"






# registration with valid email valid pass and null confirmation
def test_failed_registration_null_confirm_password():
    driver = init_registration()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123654")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("")
    # email will be created with the rd() function
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"






# registration with valid email null pass and valid confirmation
def test_failed_registration_null_password():
    driver = init_registration()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123232")
    # email will be created with the rd() function
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"





# registration with valid email null pass and null confirmation
def test_failed_registration_null_pass_null_confirm():
    driver = init_registration()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("")
    # email will be created with the rd() function
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"





# not working atm, need to locate email popup in devt
# def failed_registration_invalid_email():
#     driver = init_registration()
#     driver.find_element(By.XPATH,register_page).click()
#     driver.find_element(By.XPATH,enter_pass).send_keys("123123")
#     driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123123")
#     # illegal email (@.com) will be created with rd() function
#     driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@.com")
#     driver.find_element(By.XPATH,sign_up).click()
#     # verify the signup button is disabled
#     value = driver.find_element(By.XPATH,enter_email).get_attribute("yn")
#     assert value == true




# confirm logo picture exist
def test_logo_img():
    driver = init_registration()
    driver.find_element(By.XPATH,"//img[@id='logo']")
    img = driver.find_element(By.XPATH,"//img[@id='logo']").get_attribute("src")
    print(img)
    assert img == "https://i.ibb.co/txxHvs7/d83a35fd-1000-466d-9ceb-dd287592c18e.jpg"

