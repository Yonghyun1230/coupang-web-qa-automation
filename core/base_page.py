from playwright.sync_api import Page, expect, Locator


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def find(self, selector):
        if isinstance(selector, Locator):
            return selector

        return self.page.locator(selector)

    # 객체 노출 검증
    def verify_visible(self, selector, timeout=10000):
        expect(self.find(selector)).to_be_visible(
            timeout=timeout
        )

    def click(self, selector):
        self.find(selector).click()

    def hover(self, selector):
        self.find(selector).hover()

    def input_text(self, selector, text):
        self.find(selector).fill(text)

    def press(self, selector, key):
        self.find(selector).press(key)

    def get_text(self, selector):
        return self.find(selector).inner_text()

    def is_visible(self, selector):
        return self.find(selector).is_visible()

    def verify_visible(self, selector):
        expect(self.find(selector)).to_be_visible()

    def scroll(self, x=0, y=500):
        self.page.mouse.wheel(x, y)

    def screenshot(self, path):
        self.page.screenshot(path=path)

    def refresh(self):
        self.page.reload()

    def back(self):
        self.page.go_back()
