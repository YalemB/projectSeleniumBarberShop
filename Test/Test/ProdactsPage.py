from Test.BaseTest.base import *
driver = init()



def test_page():

    x = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]")
    actions = ActionChains(driver)
    actions.move_to_element(x)
    actions.click(x).perform()