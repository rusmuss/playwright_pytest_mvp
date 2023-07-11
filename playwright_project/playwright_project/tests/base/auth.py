import string
from _decimal import Decimal
from datetime import datetime
import re

from allure_commons.types import AttachmentType

from playwright_project import config
# from time import sleep
# from pytest_check import check
# from functools import partial
# import json

import allure
import pytest
from playwright.sync_api import Page, expect


class Auth:

    # mutable vars
    start_test_time: datetime = None
    str_var: str = ''
    decimal_var: Decimal = None

    # fixtures list
    playwright_page = None

    # constants
    dict_var = {"var1": 1, "var2": 2}

    # string templates
    # usage:
    # print(string_template_var.safe_substitute({"transaction": "123123123"}))
    string_template_var = string.Template('This is my transaction "$transaction"')

    @pytest.fixture(autouse=True)
    def before_test(self, playwright_page: Page):
        self.playwright_page = playwright_page
        self.start_test_time = datetime.utcnow()

    @pytest.fixture()
    def after_block(self, playwright_page: Page):
        yield
        print("Action after test")

    @allure.step("Description for your step Check title")
    def check_title(self):
        expect(self.playwright_page).to_have_title(re.compile(config.title))

    @allure.step("Check invalid authorization")
    def check_invalid_creds(self, user, password):
        username_element = self.playwright_page.locator('#login_field')
        password_element = self.playwright_page.locator('#password')

        username_element.clear()
        username_element.type(user)

        password_element.clear()
        password_element.type(password)

        self.playwright_page.locator(".js-sign-in-button").click()

        expect(self.playwright_page.locator('.js-flash-alert')).to_contain_text('Incorrect username or password')
