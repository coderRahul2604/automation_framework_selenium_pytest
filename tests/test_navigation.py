from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import login
from pages.navigation_bar import Navigation_bar_test, Navigation_bar_mobile_test

driver = login()

def test_nav():
    if Navigation_bar_test(driver):
        print("Navigation working fine!")
    else:
        print("Something went wrong!")
    
    if Navigation_bar_mobile_test(driver):
        print("Mobile navigation fine!")
    else:
        print("Something went wrong!")

    driver.quit()

