import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button_on_the_main_page(browser):
    browser.get(link)
    time.sleep(5)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-baske"))
    assert button > 0, 'Button add to basket not found'