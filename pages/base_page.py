class BasePage:
    def __init__(self, page):
        self.page = page

    def verify_page(self):
        self.close_cookie_banner()

    def close_cookie_banner(self, timeout=3000):
        if self.page.locator("div.cky-consent-container").is_visible(timeout=timeout):
            self.page.locator(
                'div.cky-consent-container button[aria-label="Accept All"]'
            ).click()
