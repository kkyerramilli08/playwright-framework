'''
as a part of this class LoginPage construction - I  will define all the page locators
whenever we create any object to this class LoginPage , automatically constructor will be called and
hence all the locators will be initialized and we can use them in our test cases.

as we are defining the page specific locators hence in the constructor we need to pass the page reference
'''


from playwright.sync_api import Page, expect
from utilities.ConfigReader import ConfigFileReader


class LoginPage:
        def __init__(self, page: Page):
                self.page = page
                self.username_textField = page.get_by_placeholder("Username")
                self.password_textField = page.get_by_placeholder("Password")
                self.login_button = page.get_by_role("button", name="Login")

        def login_to_application(self, username, password):
                try:
                        self.username_textField.fill(username)
                        self.password_textField.fill(password)
                        self.login_button.click()

                        config_reader = ConfigFileReader()
                        dashboard_URL = config_reader.readConfig("basic info", "dashboard_URL")
                        self.page.wait_for_url(dashboard_URL)
                        expect(self.page).to_have_url(dashboard_URL)
                except:
                        print("Error occurred while logging in to application")



                  
