
def test_single_checkbox_on_page_with_placeholder(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.navigate_to_single_checkbox_page()
    single_checkbox_page.check_only_one_checkbox_on_page()

def test_user_able_to_check_single_checkbox(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.navigate_to_single_checkbox_page()
    single_checkbox_page.check_user_able_to_select_checkbox()

def test_submit_button_always_enabled(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.navigate_to_single_checkbox_page()
    single_checkbox_page.check_submit_button_always_enabled()

def test_submit_button_clickable_when_checkbox_checked(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.navigate_to_single_checkbox_page()
    single_checkbox_page.check_submit_button_clickable_when_checkbox_checked()