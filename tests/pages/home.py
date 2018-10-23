from tests.pages.components.page import Page
from tests.parameters.locators import locator


class HomePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver, timeout=30)

    def About_element(self):
        return self.find(locator.About, timeout=30)

    def Articles_element(self):
        return self.find(locator.Articles, timeout=30)

    def Home_element(self):
        return self.find(locator.Home, timeout=30)

    def Login_element(self):
        return self.find(locator.Login, timeout=30)

    def Register_element(self):
        return self.find(locator.Register, timeout=30)

    def lead_element(self):
        return self.find(locator.lead, timeout=30)

    def login_element(self):
        return self.find(locator.login, timeout=30)

    def register_element(self):
        return self.find(locator.register, timeout=30)

    def my_flask_app_element(self):
        return self.find(locator.my_flask_app, timeout=30)

    def welcome_to_flask_app_element(self):
        return self.find(locator.welcome_to_flask_app, timeout=30)
