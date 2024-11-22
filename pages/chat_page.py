from playwright.sync_api import Page, expect

from .base_page import BasePage
from .navigation_menu import Navigation


class ChatPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.navigation = Navigation(page)
        self.tab = page.locator(".z-navigation div.flex-row p.text-volcanic-900")
        self.url = "https://coral.cohere.com"

    def verify_page(self):
        super().verify_page()
        assert (
            self.page.url.rstrip("/") == self.url
        ), f"Expected {self.url} but got {self.page.url}"
        expect(self.tab).to_have_text("Chat")

    def close_pop_up(self):
        if self.page.locator(
            'div[data-component="OnboardingModal"] button'
        ).first.is_visible():
            self.page.locator(
                'div[data-component="OnboardingModal"] button'
            ).first.click()

    def send_message(self, message: str):
        # self.page.locator('textarea').get_by_placeholder('Message...').fill(message)
        self.page.get_by_placeholder("Message...").fill(message)
        self.page.click('div[data-component="Composer"] button.flex-shrink-0')

    def get_messages(self):
        response_textarea = self.page.locator(
            'div[data-component="Content"] div[id*="message-row"]'
        ).first
        return response_textarea.text_content()
