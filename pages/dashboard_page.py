from playwright.sync_api import Page, expect

from .base_page import BasePage
from .navigation_menu import Navigation


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.navigation = Navigation(page)
        self.tab = page.locator(".z-navigation div.flex-row p.text-volcanic-900")
        self.header = page.locator(".text-h3-m")
        self.url = "https://dashboard.cohere.com"

    def verify_page(self):
        super().verify_page()
        assert self.page.url.rstrip("/") == self.url
        expect(self.tab).to_have_text("Dashboard")
        expect(self.header).to_have_text("Welcome, Artem!")
