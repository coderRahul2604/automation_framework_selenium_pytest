from pages.base import BasePage
from objects.admin_page_object import admin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.admin = admin

    def search_user(self, username=None, user_role=None, emp_name=None, status=None):

        base=BasePage(self.driver)
        self.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

        time.sleep(3)
        if username:
            self.send_text(admin.user_name_input, username)

        if user_role:
            self.click(admin.user_role, 5)
            self.select_dropdown_option(user_role)

        if emp_name:
            self.send_text(admin.emp_name, emp_name)
            self.select_autocomplete_result(emp_name)

        if status:
            self.click(admin.status, 5)
            self.select_dropdown_option(status)

        self.click(admin.submit_btn, 5)
        print(self.get_text(admin.no_of_records))
        time.sleep(5)
        return True

    def reset_search(self):
        self.click(admin.reset_btn, 5)

    def add_user(self, user_role, emp_name, status, username, password):

        # Click Add button
        self.click(admin.add_btn, 5)

        # Select User Role
        self.click(admin.add_user_role, 5)
        self.select_dropdown_option(user_role)

        # Enter Employee Name (autocomplete)
        self.send_text(admin.add_emp_name, emp_name)
        self.select_autocomplete_result(emp_name)

        # Select Status
        self.click(admin.add_status, 5)
        self.select_dropdown_option(status)

        # Username
        self.send_text(admin.add_username, username)

        # Password
        self.send_text(admin.add_password, password)
        self.send_text(admin.add_password_confirm, password)

        # Save user
        self.click(admin.add_save, 5)

        time.sleep(1)
        print(self.get_text(admin.message, 5))
        time.sleep(3)
    
    def delete_row(self, rowNo):

        delete_btn = (
            By.XPATH,
            f"(//div[@class='oxd-table-card']//i[contains(@class,'bi-trash')])[{rowNo}]"
        )

        # Wait for delete icon
        self.wait_for_clickable(delete_btn, 10)
        self.click(delete_btn)

        # Confirm delete popup
        confirm_yes = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
        self.wait_for_clickable(confirm_yes, 10)
        self.click(confirm_yes)

        # Toast message
        
        message = self.get_text(admin.message, 10)

        print("Toast:", message)
        return message


    def select_dropdown_option(self, text):
        """Select an option from the OrangeHRM dropdown list."""
        base = BasePage(self.driver)
        option = (By.XPATH, f"//div[@role='listbox']//span[normalize-space()='{text}']")
        base.is_visible(option)
        base.click(option, 2)

    def select_autocomplete_result(self, text):
        """Select autocomplete suggestion matching text."""
        item = (By.XPATH,f"//div[@role='listbox']//span[contains(text(),'{text}')]")
        base = BasePage(self.driver)
        base.click(item, 2)
