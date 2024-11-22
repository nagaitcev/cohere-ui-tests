from playwright.sync_api import Page

from .base_page import BasePage
from .dashboard_page import DashboardPage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.username_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator('button[type="submit"]')

    def navigate(self):
        self.page.context.add_cookies(
            [
                {
                    "name": "cookie_consent",
                    "value": "true",
                    "domain": "example.com",
                    "path": "/",
                }
            ]
        )
        self.page.goto("https://dashboard.cohere.com/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        with self.page.expect_navigation():
            self.login_button.click()
            # self.close_cookie_banner(timeout=5000)
        return DashboardPage(self.page)
