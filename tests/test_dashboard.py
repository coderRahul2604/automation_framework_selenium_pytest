from pages.dashboard_page import DashboardPage

def test_dashboard(driver):
    dashboard = DashboardPage(driver)
    result = dashboard.verify_dashboard()
    print(result)

    assert all(result.values())
