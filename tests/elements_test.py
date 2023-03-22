import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://b2c.passport.rt.ru/')
    page.open()
    time.sleep(15)