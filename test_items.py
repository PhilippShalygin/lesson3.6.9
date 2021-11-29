import time

from selenium import webdriver

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_if_add_is_enable(browser):
    browser.get(link)
    #time.sleep(30)

    #Проверяем что кнопка отображается и доступна
    assert browser.find_element_by_class_name("add-to-basket").is_displayed() and browser.find_element_by_class_name("add-to-basket").is_enabled()