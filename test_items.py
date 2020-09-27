import time
from selenium import webdriver

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(10) #визуальная проверка
    x = browser.find_elements_by_css_selector(".btn-add-to-basket")
    but = len(x)
    assert but > 0, "Not Found!!!"