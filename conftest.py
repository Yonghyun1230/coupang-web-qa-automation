import pytest

from playwright.sync_api import sync_playwright
from config.settings import (
    BROWSER,
    HEADLESS,
    TIMEOUT,
    VIEWPORT
)


@pytest.fixture(scope="session")
def browser_instance():

    with sync_playwright() as playwright:

        browser_type = getattr(playwright, BROWSER)

        browser = browser_type.launch(
            headless=HEADLESS
        )

        yield browser

        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance):

    context = browser_instance.new_context(
        viewport=VIEWPORT
    )

    page = context.new_page()
    page.set_default_timeout(TIMEOUT)

    yield page

    context.close()