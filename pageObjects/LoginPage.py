from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach


class LoginPage:
    username_textbox_id = 'user-name'
    password_textbox_id = 'password'
    login_button_name = 'login-button'



    def __init__(self,driver):

        self.driver = driver

    def enterUserName(self,user):

        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(user)


    def enterPassWord(self,password):

        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.login_button_name).click()

