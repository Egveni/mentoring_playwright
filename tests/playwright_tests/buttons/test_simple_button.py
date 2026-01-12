import pytest

def test_simple_button_clickable(simple_button_page):
    simple_button_page.open_page()
    simple_button_page.navigate_to_simple_button_page()
    simple_button_page.check_button_label_visible()
    simple_button_page.check_simple_button_working()