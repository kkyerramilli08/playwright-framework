from pathlib import Path
from playwright.sync_api import Page,expect

import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.InfoPage import InfoPage
from pages.OverviewPage import OverviewPage
# from utilities.ExcelData import ExcelUtility
from utilities.ExcelData import ExcelUtility

@pytest.mark.usefixtures("page")
class TestE2EClass:
    def test_e2eabout(self,page ):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        excel_data = ExcelUtility()
        workbook = Path(__file__).resolve().parent.parent / "testData" / "userinfo.xlsx"
        username = excel_data.getCellData(workbook, "Sheet1", 2, 1)
        password = excel_data.getCellData(workbook, "Sheet1", 2, 2)

        login_page.login_to_application(username=username, password=password)
        home_page.verify_about_page()
        home_page.logout_from_application()


    def test_e2eclass(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        info_page = InfoPage(page)
        overview_page = OverviewPage(page)

        excel_data = ExcelUtility()
        workbook = Path(__file__).resolve().parent.parent / "testData" / "userinfo.xlsx"
        username = excel_data.getCellData(workbook, "Sheet1", 2, 1)
        password = excel_data.getCellData(workbook, "Sheet1", 2, 2)

        login_page.login_to_application(username=username, password=password)
        home_page.add_first_product_to_cart()
        cart_page.proceed_to_checkout()
        info_page.enter_user_information()
        page.wait_for_timeout(5000)
        overview_page.placeOrder()
        home_page.logout_from_application()






