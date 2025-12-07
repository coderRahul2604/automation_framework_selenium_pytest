from selenium.webdriver.common.by import By

class navigations:

    side_bar = (By.XPATH, "//aside/nav[@role='navigation']")
    home_link = (By.XPATH, "//div[@class='oxd-sidepanel-header']/a")
    cross_tag = (By.XPATH, "//div[@class='oxd-sidepanel-header']/i")
    close_nav_tag = (By.XPATH, "//i[@class='oxd-icon bi-chevron-left']")
    mobile_view_nav =(By.XPATH, "//i[@class='oxd-icon bi-list oxd-topbar-header-hamburger']")
    nav_serach_bar =(By.XPATH, "//input[@placeholder='Search']")
    nav_options =(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']")
    nav_menu_maintenance = (By.XPATH, "//li[@class='oxd-main-menu-item-wrapper'][10]")