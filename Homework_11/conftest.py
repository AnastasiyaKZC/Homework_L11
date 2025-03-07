import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def browser_managment():
    browser.config.window_width = 1280
    browser.config.window_height = 1220
    # browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.timeout = 2.0

    yield
    browser.quit()