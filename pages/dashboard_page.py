# Dashboard_page.py
from objects.dashboard_page_object import dashboard
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import BasePage

import time

class DashboardPage(BasePage):
    

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.loc = dashboard

    def verify_dashboard(self):
        url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        base = BasePage(self.driver)

        base.open_url(url)
        # ---- 1. TIME AT WORK ----
        time_work_ok = self.are_visible(
            self.loc.time_spend_box_title,
            self.loc.time_spend_box,
            self.loc.user_name,
            self.loc.punch_out_btn
        )

        # ---- 2. QUICK LAUNCH ----
        quick_launch_ok = True
        for locator in self.loc.launch_list:
            if not self.is_visible(locator):
                quick_launch_ok = False
            

        # ---- 3. BUZZ POSTS ----
        posts = dashboard.posts_box
        buzz_ok = all(self.is_visible for p in posts)

        # ---- 4. EMPLOYEE ON LEAVE ----
        leave_ok = self.is_visible(self.loc.employeee_on_leaves_box)

        # ---- 5. EMPLOYEE DISTRIBUTION ----
        dist_ok = self.is_visible(self.loc.employee_distribution_box_title)

        # ---- 6. EMPLOYEE DISTRIBUTION BY LOCATION ----
        dist_loc_ok = self.is_visible(self.loc.employee_distribution_Location_box_title)

        # Return each result individually
        return {
            "time_work_ok": time_work_ok,
            "quick_launch_ok": quick_launch_ok,
            "buzz_ok": buzz_ok,
            "leave_ok": leave_ok,
            "dist_ok": dist_ok,
            "dist_loc_ok": dist_loc_ok
        }
