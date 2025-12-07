from pages.admin_page import AdminPage
from utils.driver_setup import get_driver


driver = get_driver()

def test_admin_actions(driver):
    admin = AdminPage(driver)
    admin.search_user(username=None,
        user_role="Admin",
        emp_name=None,
        status=None)
    
    toast = admin.delete_row(1)
    print("Result:", toast)
    # admin.add_user(user_role="Admin", emp_name="Test", status="Enabled", username="tester@45", password="test@123")

driver.quit()