from selenium.webdriver.common.by import By

class admin:

    # ---------System User Searchs----------
    user_name_input = (By.XPATH, "//label[text()='Username']/parent::*/following-sibling::*//input")
    user_role = (By.XPATH, "//label[text()='User Role']/parent::*/following-sibling::*//div[@class='oxd-select-text-input']")
    emp_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    status = (By.XPATH, "//label[text()='Status']/parent::*/following-sibling::*//div[@class='oxd-select-text-input']")
    reset_btn = (By.XPATH, "//button[normalize-space()='Reset']")
    submit_btn = (By.XPATH, "//button[normalize-space()='Search']")
    add_btn = (By.XPATH, "//button[normalize-space()='Add']")
    no_of_records = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")


    # ---------add user--------

    add_user_role=(By.XPATH, "//label[text()='User Role']/parent::*/following-sibling::*//div[@class='oxd-select-text-input']")
    add_emp_name =(By.XPATH, "//label[text()='Employee Name']/parent::*/following-sibling::*//input")
    add_status = (By.XPATH, "//label[text()='Status']/parent::*/following-sibling::*//div[contains(@class,'oxd-select-text')]")
    add_username = (By.XPATH, "//label[text()='Username']/parent::*/following-sibling::*//input")
    add_password = (By.XPATH, "//label[text()='Password']/parent::*/following-sibling::*//input")
    add_password_confirm = (By.XPATH, "//label[text()='Confirm Password']/parent::*/following-sibling::*//input")
    add_cancel = (By.XPATH, "//button[normalize-space()='Cancel']")
    add_save = (By.XPATH, "//button[normalize-space()='Save']")

    message = (By.XPATH, "//div[@class='oxd-toast-container oxd-toast-container--bottom']")