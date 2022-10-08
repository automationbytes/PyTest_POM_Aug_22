import pytest
from selenium import webdriver
from pytest_html_reporter import attach

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pageObjects.LoginPage import LoginPage
from pageObjects.homePage import homePage
from util.readConfig import readConfig
from util.GenerateLogs import LogGenerator
class TestDemoEx:
    logger = LogGenerator.loggen()
    @pytest.fixture()
    def prestep(self,setup):
        self.logger.info("------Pre Step------")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(readConfig.getUrl())
        lp = LoginPage(self.driver)
        lp.enterUserName("standard_user")
        lp.enterPassWord("secret_sauce")
        lp.clickLogin()

    def test_sortLowtoHigh(self,prestep):
        self.logger.info("------test_sortLowtoHigh------")
        hp = homePage(self.driver)
        if hp.appLogo_classname == True:
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/logo.png")
            attach(data=self.driver.get_screenshot_as_png())

            assert False
        hp.selectFilterOption("Price (low to high)")

    def test_sortHightoLow(self,prestep):
        hp = homePage(self.driver)
        hp.selectFilterOption("Price (high to low)")



