from playwright.sync_api import sync_playwright

def test_bing_title_verification(page):
    page.goto("https://bing.com")
    title = page.title()
    assert title == "Search - Microsoft Bing"
    # browser.close()
