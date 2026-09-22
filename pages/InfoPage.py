from playwright.sync_api import Page, expect
from utilities.Random_Data import Random_Data
from utilities.ConfigReader import ConfigFileReader

class InfoPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.postal_code_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def enter_user_information(self):
    # def enter_user_information(self, first_name: str, last_name: str, postal_code: str):
        try:
            random_data = Random_Data()
            first_name = random_data.get_first_name()
            last_name = random_data.get_last_name()
            postal_code = random_data.get_zip_code()
            self.page.wait_for_timeout(5000)
            self.first_name_field.fill(first_name)
            self.last_name_field.fill(last_name)
            self.postal_code_field.fill(postal_code)
            self.continue_button.click()
            config_reader = ConfigFileReader()
            overview_URL = config_reader.readConfig("basic info", "overviewURL")
            expect(self.page).to_have_url(overview_URL)
        except:
            print("Error occurred while entering user information")

