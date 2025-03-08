import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.set_capability("selenoid:options", selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.set_driver(driver)
    yield browser

    browser.quit()
