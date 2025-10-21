from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect, Page, Route
import re

# def test_request(page: Page):
#     page.goto("https://edube.org/login")
#     page.locator("#email").fill("ksenilin@gmail.com")
#     page.locator("#password").fill("nmd5yPSzHLt.znF")
#     page.get_by_role(role= "button", name="Log in").click()
#     sleep(5)


def test_request_backend(page: Page):
    def change_request(route: Route):
        # Only modify POST requests, let GET requests through normally
        if route.request.method == "POST":
            data = route.request.post_data
            if data:
                data = data.replace("ksenilin%40gmail.com", "xenilin%40gmail.com")
                route.continue_(post_data=data)
            else:
                route.continue_()
        else:
            route.continue_()

    # Use a more specific pattern to avoid intercepting the initial page load
    page.route("**/login", change_request)
    page.goto("https://edube.org/login")
    page.locator("#email").fill("ksenilin@gmail.com")
    page.locator("#password").fill("nmd5yPSzHLt.znF")
    page.get_by_role(role= "button", name="Log in").click()
    sleep(5)