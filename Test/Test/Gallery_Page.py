from Test.BaseTest.base import *


# verify all photos on gallery, sleep() must be used'..


def test_image1_img():
    # this part i copy from ProductPage tests
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    ### thie WebDriverWait fail without sleep
    # img = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/img[1]"))
    # ).get_attribute("src")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/tmWjrcQ/gallery-pic-1.jpg"




def test_image2_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[2]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[2]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/094VLGS/gallery-pic-2.jpg"



def test_image3_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[3]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[3]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/ZmNV2xb/gallery-pic-3.jpg"



def test_image4_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[4]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[4]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/cvtN2Vm/gallery-pic-4.jpg"



def test_image5_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[5]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[5]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/nDGZHmX/gallery-pic-5.jpg"




def test_image6_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[6]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[6]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/hLtQ9Dx/gallery-pic-6.jpg"




def test_image7_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[7]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[7]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/NTcYNNR/gallery-pic-7.jpg"




def test_image8_img():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    ### without sleep test fail
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[8]/img[1]")
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[8]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/wBFyf2w/gallery-pic-8.jpg"
