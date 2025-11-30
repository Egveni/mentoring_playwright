def test_three_checkboxes_on_page_with_labels(checkboxes_page):
    checkboxes_page.open_page()
    checkboxes_page.navigate_to_checkboxes_page()
    checkboxes_page.check_three_checkboxes_on_page()
    checkboxes_page.check_labels_of_checkboxes()

def test_user_able_to_select_each_checkbox(checkboxes_page):
    checkboxes_page.open_page()
    checkboxes_page.navigate_to_checkboxes_page()
    checkboxes_page.check_user_able_to_select_each_checkbox()

def test_submit_button_always_enabled_on_checkboxes_page(checkboxes_page):
    checkboxes_page.open_page()
    checkboxes_page.navigate_to_checkboxes_page()
    checkboxes_page.check_submit_button_always_enabled()

def test_submit_button_clickable_when_no_checkbox_checked(checkboxes_page):
    checkboxes_page.open_page()
    checkboxes_page.navigate_to_checkboxes_page()
    checkboxes_page.check_submit_button_clickable_when_no_checkbox_checked()

def test_submit_button_clickable_when_checkboxes_checked_one_by_one(checkboxes_page):
    checkboxes_page.open_page()
    checkboxes_page.navigate_to_checkboxes_page()
    checkboxes_page.check_submit_button_clickable_when_checkbox_checked_one_by_one()