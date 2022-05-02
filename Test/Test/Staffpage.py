from Test.BaseTest.base import *

#1
def test_navbar():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]").click()
    navbar = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert navbar == "Home Staff Products Gallery"
    sleep(5)

#2
def test_sign():
    driver = init()
    sign = driver.find_element(By.XPATH,"//span[contains(text(),'wondemagen barbershop')]").get_attribute("innerText")
    assert sign == "wondemagen barbershop"

#3
def test_staftext():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]").click()
    text = driver.find_element(By.XPATH,"//h4[contains(text(),'Staff')]").get_attribute("innerText")
    assert text == "Staff"

#4
def test_avielfacebook_link():
    driver = init()
    link = "//body[1]/div[1]/div[1]/div[1]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,link)))

    driver.find_element(By.XPATH,link).click()

#5
def test_avielinstagram_link():
    driver = init()
    link = "//body/div[@id='root']/div[1]/div[3]/div[1]/a[2]"
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
    driver.find_element(By.XPATH,link).click()

#6
def test_osherfacebook_link():
    driver = init()
    link = "//body/div[@id='root']/div[1]/div[4]/div[1]/a[1]"
    driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
    driver.find_element(By.XPATH,link).click()

#7
def test_osherinstagram_link():
    driver = init()
    link = "//body/div[@id='root']/div[1]/div[4]/div[1]/a[2]"
    driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
    driver.find_element(By.XPATH,link).click()

#8
def test_buttompageText():
    driver = init()
    driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]").click()
    driver.implicitly_wait(2)
    text = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[5]/h3[1]").get_attribute("innerText")
    assert text == "Here you can hear some of the mixes and sets by DJ Aviel Wondemagen"

#9
def test_soundcloud_link():
    driver = init()
    driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[5]/a[1]").click()
    driver.implicitly_wait(2)

#10
def test_youtubeLink():
    driver = init()
    driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[5]/a[2]").click()
    driver.implicitly_wait(2)



