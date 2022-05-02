from Test.BaseTest.base import *
driver = init()

#1
def test_shavingGel():
    x = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(x)
    actions.click(x).perform()
    driver.implicitly_wait(4)
    img = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/img[1]").get_attribute("src")
    driver.implicitly_wait(4)
    print(img)
    assert img == "https://i.ibb.co/txxHvs7/d83a35fd-1000-466d-9ceb-dd287592c18e.jpg"
    driver.implicitly_wait(2)
    driver.quit()

#2
def test_dramaRoll():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/R9ybqJS/Drama-Roller-for-the-beard-for-opening-pores.jpg"

#3
def test_hairwax():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/d0G8BQ1/Hair-wax-extra-strong.jpg"

#4
def test_clay():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/5R51KLt/Clay-for-hair-styling.jpg"

#5
def test_Professional_Shaver():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[5]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/ngypr2N/Professional-rechargeable-haircut-machine-for-finishing-with-Wahl-8171-T-knife.png"

#6
def test_BarberPRO_CutClean():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/5R51KLt/Clay-for-hair-styling.jpg"

#7
def test_Wahl_Cordless():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[7]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/J3TZt7q/Wahl-Cordless-Magic-Clip-81448-haircut-machine.png"

#8
def test_Professional_rechargeable():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[8]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/1LGkb2z/Professional-Sassonic-ESE1002-Shaver-and-Finisher.jpg"

#9
def test_sponge():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[9]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/NKP8nmM/Sponge-for-frizzy-and-afro-hair-styling-Barber-PRO-Q126.jpg"

#10
def test_Schwarzkopf_Spray():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[10]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/NYSCm9Z/Super-Hold-Schwarzkopf-Silhouette-Spray.jpg"

#11
def test_Hair_clipper():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[11]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/bQ2cb5r/Hair-clipper-for-nose-and-ears-Sassonic-Sassonic-ESE011.jpg"

#12
def test_Keratin_Beard_Oil():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[12]/img[1]").get_attribute("src")
    assert img == "https://i.ibb.co/K7Sm9yn/Redone-Keratin-Beard-Oil.jpg"

