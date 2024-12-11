import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestItems:

    def test_find_element(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

        assert True
