import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, Config, Browser


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
   options.capabilities.update(selenoid_capabilities)
   driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

   browser = Browser(Config(driver))
   yield browser

   browser.quit()

    # browser.config.window_width = 1280
    # browser.config.window_height = 1220
    # # browser.config.base_url = "https://demoqa.com/automation-practice-form"
    # browser.config.timeout = 2.0
    #
    # yield
    # browser.quit()