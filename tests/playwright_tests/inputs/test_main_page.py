
def test_welcome_text(main_page):
    main_page.open_page()
    main_page.check_welcome_text()


def test_text_input(main_page):
    main_page.open_page()
    main_page.text_input_clickable()