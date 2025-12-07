from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------------- Utility to support locator OR WebElement ---------------- #

    def _get_element(self, locator, timeout=10):
        """Return WebElement whether a locator tuple OR WebElement is passed."""
        if isinstance(locator, tuple):  # locator
            return self.wait_for_element(locator, timeout)
        return locator  # already a WebElement

    # ---------------- Visibility & waits ---------------- #

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def are_visible(self, *locators, timeout=10):
        return all(self.is_visible(locator, timeout) for locator in locators)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # ---------------- Element actions ---------------- #

    def click(self, locator, timeout=10):
        """Click element (supports locator OR WebElement)."""
        if isinstance(locator, tuple):
            element = self.wait_for_clickable(locator, timeout)
        else:
            element = locator
        element.click()

    def js_click(self, locator, timeout=10):
        element = self._get_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def send_text(self, locator, text, clear=True, timeout=10):
        element = self._get_element(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = self._get_element(locator, timeout)
        return element.text

    def get_attribute(self, locator, attribute, timeout=10):
        element = self._get_element(locator, timeout)
        return element.get_attribute(attribute)

    # ---------------- Advanced interaction ---------------- #

    def hover(self, locator, timeout=10):
        element = self._get_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator, timeout=10):
        element = self._get_element(locator, timeout)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator, timeout=10):
        element = self._get_element(locator, timeout)
        ActionChains(self.driver).context_click(element).perform()

    # ---------------- Navigation utilities ---------------- #

    def open_url(self, url):
        """Navigate to a URL."""
        self.driver.get(url)

    def go_back(self):
        """Browser back navigation."""
        self.driver.back()

    def go_forward(self):
        """Browser forward navigation."""
        self.driver.forward()

    def refresh(self):
        """Refresh the current page."""
        self.driver.refresh()

    def get_current_url(self):
        """Return current URL."""
        return self.driver.current_url

    def get_title(self):
        """Return current page title."""
        return self.driver.title

    def wait_for_url(self, url_substring, timeout=10):
        """Wait until URL contains a specific text."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url_substring)
            )
            return True
        except TimeoutException:
            return False
