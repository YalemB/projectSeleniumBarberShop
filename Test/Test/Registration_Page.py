







#random email address will be added to the @mail.com
def rd():
    b = ""
    while len(b) < 9:
        a = randint(0, 9)
        b = b + str(a)
    return b




# all buttons in register section
register_page = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[2]"
enter_pass = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[1]"
enter_confirm_pass = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[2]"
enter_email = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[3]"
sign_up = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[4]"
logout_button = "//button[contains(text(),'log out')]"


# registration with valid information
def successful_registration():
    driver = init()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123123")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123123")
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify you registered and the logout button appear
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,logout_button))
    ).get_attribute("innerText")
    assert value == "log out"
    sleep(2)


# registration with valid email and unmatched passwords
def failed_registration_valid_email_unmatched_password():
    driver = init()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123654")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123232")
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"
    sleep(2)





def failed_registration_null_fields():
    driver = init()
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
    sleep(2)





# registration with valid email valid pass and null confirmation
def failed_registration_null_confirm_password():
    driver = init()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123654")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("")
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"
    sleep(2)





# registration with valid email null pass and valid confirmation
def failed_registration_null_password():
    driver = init()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123232")
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"
    sleep(2)






# registration with valid email null pass and null confirmation
def failed_registration_null_pass_null_confirm():
    driver = init()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("")
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@mail.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    value = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,sign_up))
    ).get_attribute("disabled")
    assert value == "true"
    sleep(2)









#not working
def failed_registration_invalid_email():
    driver = init()
    driver.find_element(By.XPATH,register_page).click()
    driver.find_element(By.XPATH,enter_pass).send_keys("123123")
    driver.find_element(By.XPATH,enter_confirm_pass).send_keys("123123")
    driver.find_element(By.XPATH,enter_email).send_keys(f"{rd()}@.com")
    driver.find_element(By.XPATH,sign_up).click()
    # verify the signup button is disabled
    v = driver.find_element(By.CLASS_NAME,"btn").rect.keys()
    print(list(v))
    print(len(list(v)))
    # assert value == "invalid__bubble"
    sleep(8)
failed_registration_invalid_email()

def logo_img():
    driver = init()
    driver.find_element(By.XPATH,"//img[@id='logo']")
    img = driver.find_element(By.XPATH,"//img[@id='logo']").get_attribute("src")
    print(img)
    assert img == "https://i.ibb.co/txxHvs7/d83a35fd-1000-466d-9ceb-dd287592c18e.jpg"
