
def test_disabled_button_not_working_by_default(disabled_button_page):
    disabled_button_page.open_page()
    disabled_button_page.navigate_to_disabled_button_page()
    disabled_button_page.check_disabled_button_not_working_by_default()

def test_enable_disable_disabled_button(disabled_button_page):
    disabled_button_page.open_page()
    disabled_button_page.navigate_to_disabled_button_page()
    disabled_button_page.enable_disabled_button()
    disabled_button_page.disable_disabled_button()

def test_pressing_submit_button_when_enabled(disabled_button_page):
    disabled_button_page.open_page()
    disabled_button_page.navigate_to_disabled_button_page()
    disabled_button_page.enable_disabled_button()
    disabled_button_page.press_submit_button_and_check_success()