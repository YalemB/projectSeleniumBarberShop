from Test.BaseTest.base import *


def test_navbar():
    driver = init()
    navbar = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert navbar == "Home Staff Products Gallery"

#2
def test_logo():
    driver = init()
    logo = driver.find_element(By.XPATH,"//span[contains(text(),'wondemagen barbershop')]").get_attribute("innerText")
    assert logo == "wondemagen barbershop"

#3
def test_homesign():
    driver = init()
    homesign = driver.find_element(By.XPATH,"//h4[contains(text(),'Home')]").get_attribute("innerText")
    assert homesign == "Home"

#?
# def test_PhotoSlide():
#     driver = init()
#     photos = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[2]/div[4]/img[1]").get_attribute("src")
#     assert photos == "<div id=\"frame\"><img src=\"https://i.ibb.co/d7Q5dVz/slider-pic-1.jpg\"></div><div id=\"frame\"><img src=\"https://i.ibb.co/SQmRHjS/slider-pic-2.jpg\"></div><div id=\"frame\"><img src=\"https://i.ibb.co/SdLpGsK/slider-pic-3.jpg\"></div><div id=\"frame\"><img src=\"https://i.ibb.co/pyzLbpj/slider-pic-4.jpg\"></div><div id=\"frame\"><img src=\"https://i.ibb.co/g4GhBLF/slider-pic-5.jpg\"></div>"

#4
def test_PhoneNumber():
    driver = init()
    aviel = driver.find_element(By.XPATH,"//a[contains(text(),'+972 53-624-0281')]").get_attribute("innerText")
    assert aviel == "+972 53-624-0281"
    osher = driver.find_element(By.XPATH,"//a[contains(text(),'+972 53-221-0440')]").get_attribute("innerText")
    assert osher == "+972 53-221-0440"

#?
# def test_about():
#     driver = init()
#     about = driver.find_element(By.ID,"//div[@id='about']").get_attribute("innerText")
#     assert about == "About the barbershop..We invite you to be impressed by a young and colorful men's barbershop,innovative and full of style.waiting for you.."

#5
def test_facebooklink():
    facebooklink = "//body[1]/div[1]/div[1]/div[3]/footer[1]/section[1]/a[1]/img[1]"
    tiktoklink = ""
    driver = init()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,facebooklink)))
    driver.find_element(By.XPATH,facebooklink).click()

#6
def test_instagramlink():
    driver = init()
    instargramlink = "//body[1]/div[1]/div[1]/div[3]/footer[1]/section[1]/a[2]/img[1]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,instargramlink)))
    driver.find_element(By.XPATH,instargramlink).click()

#7
def test_tiktoklink():
    driver = init()
    tiktoklink = "//body[1]/div[1]/div[1]/div[3]/footer[1]/section[1]/a[3]/img[1]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,tiktoklink)))
    driver.find_element(By.XPATH,tiktoklink).click()



