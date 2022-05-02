from Test.BaseTest.base import *

#1
def test_shavingGel():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    img = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/img[1]").get_attribute("src")
    print(img)
    assert img == "https://i.ibb.co/txxHvs7/d83a35fd-1000-466d-9ceb-dd287592c18e.jpg"
    driver.implicitly_wait(20)
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h4[1]").get_attribute("innerText")
    print(text)
    assert text == "500 ml shaving gel with a male fragrance RedOne"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/h4[2]").get_attribute(
        "innerText")
    print(price)
    assert price == "49 NIS"
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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/h4[1]").get_attribute("innerText")
    assert text == "Drama Roller for the beard for opening pores"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/h4[2]").get_attribute(
        "innerText")
    assert price == "28 NIS"

    driver.quit()
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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/h4[1]").get_attribute("innerText")
    assert text == "Hair wax - extra strong"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/h4[2]").get_attribute(
        "innerText")
    assert price == "49 NIS"
    driver.quit()

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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/h4[1]").get_attribute("innerText")
    assert text == "Clay for hair styling"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/h4[2]").get_attribute(
        "innerText")

    assert price == "70 NIS"
    driver.quit()

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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[5]/h4[1]").get_attribute("innerText")
    assert text == "Professional Sassonic ESE1002 Shaver and Finisher"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[5]/h4[2]").get_attribute(
        "innerText")
    assert price == "349 NIS"
    driver.quit()

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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[6]/h4[1]").get_attribute("innerText")
    assert text == "BarberPRO CutClean Z300 Barber Pro haircut machine"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[6]/h4[2]").get_attribute(
        "innerText")
    assert price == "299 NIS"

    driver.quit()

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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[7]/h4[1]").get_attribute("innerText")
    assert text == "Wahl Cordless Magic Clip 81448 haircut machine"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[7]/h4[2]").get_attribute(
        "innerText")
    assert price == "570 NIS"

    driver.quit()

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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[8]/h4[1]").get_attribute("innerText")
    assert text == "Professional rechargeable haircut machine for finishing with Wahl 8171 T knife"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[8]/h4[2]").get_attribute(
        "innerText")
    assert price == "550 NIS"

    driver.quit()


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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[9]/h4[1]").get_attribute("innerText")
    assert text == "Sponge for frizzy and afro hair styling BarberPRO Q126"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[9]/h4[2]").get_attribute(
        "innerText")
    assert price == "29 NIS"

    driver.quit()


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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[10]/h4[1]").get_attribute("innerText")
    assert text == "Super Hold Schwarzkopf Silhouette Spray"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[10]/h4[2]").get_attribute(
        "innerText")
    assert price == "55 NIS"

    driver.quit()
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
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[11]/h4[1]").get_attribute("innerText")
    assert text == "Hair clipper for nose and ears Sassonic Sassonic ESE011"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[11]/h4[2]").get_attribute(
        "innerText")
    assert price == "85 NIS"

    driver.quit()

#12
def test_Keratin_Beard_Oil():
    driver = init()
    path = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(path)
    actions.click(path).perform()
    driver.implicitly_wait(20)
    img = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[12]/img[1]").get_attribute("src")
    print("")
    print(img)
    assert img == "https://i.ibb.co/K7Sm9yn/Redone-Keratin-Beard-Oil.jpg"
    text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[12]/h4[1]").get_attribute("innerText")
    print(text)
    assert text == "Redone Keratin Beard Oil"
    price = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[12]/h4[2]").get_attribute(
        "innerText")
    print(price)
    assert price == "79 NIS"

    driver.quit()