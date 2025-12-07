import pytest
from utils.driver_setup import login

@pytest.fixture
def driver():
    driver = login()
    yield driver
    driver.quit()
