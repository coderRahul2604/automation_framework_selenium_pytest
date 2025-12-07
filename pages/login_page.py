# login_page_action.py
from objects.login_page_objects import LoginObjects
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.loc = LoginObjects()

    def enter_username(self, username):
        el = self.wait.until(EC.visibility_of_element_located(self.loc.username))
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        el = self.wait.until(EC.visibility_of_element_located(self.loc.password))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.loc.login_btn))
        btn.click()

    def login_page_actions(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(3)
