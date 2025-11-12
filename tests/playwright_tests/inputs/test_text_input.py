import pytest

def test_text_input(simple_page):
    simple_page.open_page()
    simple_page.check_text_input_page_visibility()
    simple_page.navigate_to_text_input_page()
    simple_page.check_text_input_working()

@pytest.mark.parametrize("valid_text", [
    "test",
    "Test123",
    "user_name",
    "my-value",
    "Test_123-abc",
    "valid_input-123",
])

def test_valid_inputs(simple_page, valid_text):
    simple_page.open_page()
    simple_page.check_text_input_page_visibility()
    simple_page.navigate_to_text_input_page()
    simple_page.check_no_error_visible_for_valid_inputs(valid_text)

@pytest.mark.parametrize("invalid_text", [
    ("test@mail"),
    ("hello world"),
    ("тест"),
    ("test!"),
    ("value#123"),
    ("test.com"),
    ("user$name"),
])
def test_invalid_inputs(simple_page, invalid_text):
    simple_page.open_page()
    simple_page.navigate_to_text_input_page()
    simple_page.check_error_visible_for_invalid_inputs(invalid_text)

@pytest.mark.parametrize("length,should_pass,expected_error", [
    (1, False, "Please enter 2 or more characters"),  
    (2, True, None),
    (3, True, None),
    (10, True, None),
    (24, True, None),
    (25, True, None),
    (26, False, "Please enter no more than 25 characters"),
    (30, False, "Please enter no more than 25 characters"),
])
def test_text_length_validation(simple_page, length, should_pass, expected_error):
    simple_page.open_page()
    simple_page.navigate_to_text_input_page()
    simple_page.check_text_length_validation(length, should_pass, expected_error)