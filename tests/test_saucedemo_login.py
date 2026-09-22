# from playwright.sync_api import sync_playwright
# from pytest_playwright.pytest_playwright import browser

def test_saucedemo_login_flow(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # FIX: Change the URL string to match exactly what the browser outputs
    assert page.url == "https://www.saucedemo.com/inventory.html"
    page.wait_for_timeout(5000)
