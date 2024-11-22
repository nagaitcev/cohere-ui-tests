from playwright.sync_api import Page, expect

from .base_page import BasePage
from .navigation_menu import Navigation


class PlaygroundPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.navigation = Navigation(page)
        self.tab = page.locator(".z-navigation div.flex-row p.text-volcanic-900")
        self.url = "https://dashboard.cohere.com/playground/chat"

    def verify_page(self):
        super().verify_page()
        assert self.page.url.rstrip("/") == self.url
        expect(self.tab).to_have_text("Playground")
