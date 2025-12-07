from selenium.webdriver.common.by import By
import time
from pages.base import BasePage 
from objects.navigation_objects import navigations

def Navigation_bar_test(driver):
    base = BasePage(driver)
    nav = navigations

    by, base_xpath = nav.nav_options
    elements = driver.find_elements(by, base_xpath)
    total = len(elements)

    for i in range(1, total + 1):
        xpath = f"({base_xpath})[{i}]"

        element = driver.find_element(By.XPATH, xpath)

        if i == 10:
            print("Clicking on Maintenance - requires password")
            
            base.click(element, 5)
            time.sleep(1)
            base.go_back()
            time.sleep(1)

            # After going back → re-find menu elements
            elements = driver.find_elements(by, base_xpath)
            continue 

        base.click(element,5)
        time.sleep(1)

    txt="Admin"
    base.send_text(navigations.nav_serach_bar, txt)
    search_result = base.get_text(navigations.nav_options)

    base.click(navigations.close_nav_tag, 3)
    time.sleep(3)

    return txt==search_result

def Navigation_bar_mobile_test(driver):
    base = BasePage(driver)
    base.refresh()
    driver.set_window_size(400, 900)
    time.sleep(1)

    by, base_xpath = navigations.nav_options

    total = len(driver.find_elements(by, base_xpath))

    try:
        for i in range(total):

            # Open the mobile menu
            base.click(navigations.mobile_view_nav, 3)
            time.sleep(0.6)    

            elements = driver.find_elements(by, base_xpath)
            element = elements[i]     

            if i == 9: 
                print("Clicking on Maintenance - requires password")

                base.click(element, 5)
                time.sleep(1)

                base.go_back()
                time.sleep(1)
                base.refresh()

                elements = driver.find_elements(by, base_xpath)
                continue


            base.click(element, 5)
            time.sleep(0.8)

        base.click(navigations.mobile_view_nav, 5)
        time.sleep(3)
        base.click(navigations.cross_tag, 5)
        time.sleep(3)

        return True
    
    except:
        return False

    

    

