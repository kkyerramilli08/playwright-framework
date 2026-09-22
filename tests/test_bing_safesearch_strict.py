from playwright.sync_api import Page
import time


def test_navigate_to_bing_safesearch_settings_select_strict_radio_button_and_wait(page: Page):
    # Navigate to Bing SafeSearch settings
    page.goto("https://www.bing.com/account/general?ru=")

    # Wait for the page to load
    page.wait_for_load_state("networkidle")

    # Select Strict radio button - try multiple possible selectors
    try:
        # Try clicking the label or radio button for Strict SafeSearch
        page.click("text=/.*Strict.*/i", timeout=5000)
    except:
        try:
            page.click("#strict", timeout=5000)
        except:
            try:
                page.click("input[type='radio'][id*='strict' i]", timeout=5000)
            except:
                # Try finding radio button with value strict (case insensitive)
                page.click("input[type='radio'][value*='strict' i]", timeout=5000)

    # Wait for 5 seconds
    time.sleep(5)
