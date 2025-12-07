from selenium.webdriver.common.by import By

class dashboard:

    time_spend_box_title = (By.XPATH, "//p[normalize-space()='Time at Work']")
    user_name = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-attendance-card-state']")
    punch_out_btn = (By.XPATH, "//button[contains(@type,'button')]//i[contains(@class,'oxd-icon bi-stopwatch')]")
    time_spend_box = (By.XPATH, "//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-dashboard-widget'][1]")
    punch_out_time = (By.XPATH, "//div[@class='oxd-time-input']")

    my_action_box_title = (By.XPATH, "//p[contains(@class,'oxd-text oxd-text--p') and contains(normalize-space(.), 'My Action')]")
    to_do_list = (By.XPATH, "//div[@class='orangehrm-todo-list']")

    quicky_launch_box_title = (By.XPATH, "//p[contains(@class,'oxd-text oxd-text--p') and contains(normalize-space(.), 'Quick Launch')]")
    quicky_launch_box = (By.XPATH, "//div[@class='oxd-grid-3 orangehrm-quick-launch']")
    assign_leaves = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-quick-launch-card'][1]")
    leaves_list = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-quick-launch-card'][2]")
    timesheet = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-quick-launch-card'][3]")
    apply_leaves = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-quick-launch-card'][4]")
    my_leaves = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-quick-launch-card'][5]")
    my_timesheets = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-quick-launch-card'][6]")
    launch_list = [assign_leaves, leaves_list, timesheet, my_leaves, my_timesheets]

    Buzz_latest_post_box_title = (By.XPATH, "//p[contains(@class,'oxd-text oxd-text--p') and contains(normalize-space(.), 'Buzz Latest Posts')]")
    posts_box = (By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-buzz-widget-card']")

    employee_on_leaves_box_title = (By.XPATH, "//p[contains(@class,'oxd-text oxd-text--p') and contains(normalize-space(.), 'Employees on Leave Todayt')]")
    employeee_on_leaves_box = (By.XPATH, "//div[contains(@class, 'orangehrm-dashboard-widget-body')]//div[contains(@class, 'orangehrm-dashboard-widget-body-nocontent')]")

    employee_distribution_box_title = (By.XPATH, "//p[contains(normalize-space(), 'Employee Distribution by Sub Unit')]")
    emp_dist_chart = (By.XPATH, "//canvas[@id='GDsC2heq']")

    employee_distribution_Location_box_title = (By.XPATH, ("//p[contains(normalize-space(), 'Employee Distribution by Location')]"))
    emp_dist_loction_chart = (By.XPATH, "//canvas[@id='xJHGEX-3']")


    