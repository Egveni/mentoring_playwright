from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext

#second value needed for a new tab
#if you want to work wit the first tab only, you can use just "page" as a parameter
# if you want to wok with a second tab, you need to add "new_tab" as a parameter
def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://nomads.com/")
    with context.expect_page() as new_tab_event:
        page.get_by_alt_text("Get insured").click()
        new_tab = new_tab_event.value
    new_tab.get_by_role("link", name="Sign me up").click()


    