from playwright.sync_api import Playwright, sync_playwright, Page
from pages.like_a_button import LikeAButton



def test_like_a_button(page: Page):
    like_a_button = LikeAButton(page)
    like_a_button.open()
    like_a_button.check_button_visible()



def test_like_a_button_click_and_check_result(page: Page):
    like_a_button = LikeAButton(page)
    like_a_button.open()
    like_a_button.click_the_button()
    like_a_button.check_result_text_is_("Submitted")