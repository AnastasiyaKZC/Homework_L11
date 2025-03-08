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
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Привязываем WebDriver к Selene
    browser.config.driver = driver
    browser.config.window_width = 1280
    browser.config.window_height = 1220
    browser.config.timeout = 2.0

    yield browser  # Передаём в тест настроенный browser

    driver.quit()  # Закрываем WebDriver
