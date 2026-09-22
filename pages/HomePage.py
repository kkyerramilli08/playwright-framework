from playwright.sync_api import Page, expect
from utilities.ConfigReader import ConfigFileReader


class HomePage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_container")
        self.menu_button = page.get_by_role("button", name="Menu")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.about_link = page.get_by_role("link", name="About")


    def add_first_product_to_cart(self):
        try:
            self.add_to_cart_button.first.click()
            self.shopping_cart_icon.click()
            Config_reader = ConfigFileReader()
            cart_URL = config_reader.readconfig("basic info", cartURL)
            expect(self.page).to_have_URL(cart_URL)
        except:
            print("Error occurred while adding product to cart")

    def logout_from_application(self):
        try:
            self.menu_button.click()
            self.logout_link.click()
        except:
            print("Error occurred while logging out from application")

    def verify_about_page(self):
        try:
            self.menu_button.click()
            self.about_link.click()
            config_reader = ConfigFileReader()
            about_URL = config_reader.readConfig("basic info", "aboutURL")
            expect(self.page).to_have_url(about_URL)
            self.page.go_back()
        except:
            print("Error occurred while verifying about page")
