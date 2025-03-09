import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # browser = Browser(Config(driver=driver))  # исправлено название переменной
    browser = Browser(Config())
    browser.config.driver = driver  # Назначаем driver отдельно
    yield browser  # фикстура отдаёт browser

    browser.quit()  # закрытие драйвера после теста