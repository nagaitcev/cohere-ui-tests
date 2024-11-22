class Navigation:
    def __init__(self, page):
        self.page = page

    def click_chat(self):
        with self.page.expect_navigation():
            self.page.locator(".z-navigation div.flex-row").get_by_text("Chat").click()
        from .chat_page import ChatPage

        return ChatPage(self.page)

    def click_dashboard(self):
        with self.page.expect_navigation():
            self.page.locator(".z-navigation div.flex-row").get_by_text(
                "Dashboard"
            ).click()
        from .dashboard_page import DashboardPage

        return DashboardPage(self.page)

    def click_playground(self):
        with self.page.expect_navigation():
            self.page.locator(".z-navigation div.flex-row").get_by_text(
                "Playground"
            ).click()
        from .playground_page import PlaygroundPage

        return PlaygroundPage(self.page)

    def click_docs(self):
        with self.page.expect_navigation():
            self.page.locator(".z-navigation div.flex-row").get_by_text("Docs").click()
        from .docs_page import DocsPage

        return DocsPage(self.page)

    def click_community(self):
        with self.page.expect_navigation():
            self.page.locator(".z-navigation div.flex-row").get_by_text(
                "Community"
            ).click()
        from .community_page import CommunityPage

        return CommunityPage(self.page)

    def expand_user_menu(self):
        self.page.locator(
            '.z-navigation div.flex-row div[data-component="NavigationUserMenu"] button'
        ).click()
        return UserMenu(self.page)


class UserMenu:
    def __init__(self, page):
        self.page = page

    def click_logout(self):
        with self.page.expect_navigation():
            self.page.get_by_text("Log out").first.click()
        from .login_page import LoginPage

        return LoginPage(self.page)
