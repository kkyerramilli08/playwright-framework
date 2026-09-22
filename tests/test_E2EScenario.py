
from pathlib import Path
import requests

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.InfoPage import InfoPage
from pages.OverviewPage import OverviewPage
from utilities.ExcelData import ExcelUtility

excel = ExcelUtility()

# from utilities.ExcelData import getCellData
# from utilities.Random_Data import Random_Data



def test_e2escenario(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)
    info_page = InfoPage(page)
    overview_page = OverviewPage(page)

    workbook = Path(__file__).resolve().parent.parent / "testData" / "userinfo.xlsx"
    # Change this line:
    # username = getCellData(workbook, "Sheet1", 2, 1)

    # To this:
    username = excel.getCellData(workbook, "Sheet1", 2, 1)

    # username = getCellData(workbook, "Sheet1", 2, 1)
    password = excel.getCellData(workbook, "Sheet1", 2, 2)

    login_page.login_to_application(username=username, password=password)
    #login_page.login_to_application(username="standard_user", password="secret_sauce")
    home_page.add_first_product_to_cart()
    cart_page.proceed_to_checkout()
    info_page.enter_user_information()
    page.wait_for_timeout(5000)
    # info_page.enter_user_information(first_name="kamal", last_name="kiran", postal_code="560100")
    overview_page.placeOrder()

    # 1. Put your webhook URL path into a clean variable (can override with N8N_WEBHOOK_URL)
    import os
    n8n_url = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook-test/0c48f4a1-6f55-4aa4-812a-540f754ad4d1")

    # 2. Package your simple learning payload data
    data_payload = {"message": "SauceDemo test completed successfully!"}

    # 3. Fire the request directly to n8n with timeout and error handling
    try:
        requests.post(n8n_url, json=data_payload, timeout=5)
    except requests.RequestException as e:
        print("n8n POST failed:", e)

