
def test_looks_like_button_clickable(looks_like_button_page):
    looks_like_button_page.open_page()
    looks_like_button_page.navigate_to_looks_like_button_page()
    looks_like_button_page.check_button_label_visible()
    looks_like_button_page.check_looks_like_button_working()