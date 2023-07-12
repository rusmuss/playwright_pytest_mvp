import pytest
import uuid
import allure
import requests
from playwright.sync_api import Playwright, Page, sync_playwright
from playwright_project import config


@pytest.fixture(scope="session")
def request_session():
    return requests.Session()


@pytest.fixture(scope="function", params=config.BROWSER_LIST)
def app_page(playwright: Playwright, request) -> Page:
    browser = playwright[request.param].launch(headless=config.HEADLESS_MODE)
    context = browser.new_context()

    page = context.new_page()

    page.goto(config.SITE_URL)
    yield page
    if request.node.rep_call.failed:
        file_name = f"{request.node.name}{uuid.uuid4()}"
        screenshot = page.screenshot(path=f"screenshots/{file_name}.png", full_page=True)
        # video = p.video.path()
        allure.attach(screenshot, name=f"{file_name}", attachment_type=allure.attachment_type.PNG)
    page.close()
    browser.close()
