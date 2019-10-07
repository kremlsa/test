import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button_on_the_main_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert basket_button, "Button add to basket not found"
