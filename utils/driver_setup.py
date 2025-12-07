from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.base import BasePage

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

def login():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = get_driver()
    driver.get(url)

    login_page = LoginPage(driver)
    login_page.login_page_actions("Admin", "admin123")

    assert "dashboard" in driver.current_url.lower()
    return driver 
