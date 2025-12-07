
from selenium.webdriver.common.by import By

class LoginObjects:

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    #forgotpass = (By.XPATH("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"))
    