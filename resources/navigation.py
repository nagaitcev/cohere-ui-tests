from pages.dashboard_page import DashboardPage


class PageFactory:
    def __init__(self, page):
        self.page = page

    def go_to_chat(self):
        return DashboardPage(self.page).navigation.click_chat()

    def go_to_dashboard(self):
        return DashboardPage(self.page).navigation.click_dashboard()

    def go_to_playground(self):
        return DashboardPage(self.page).navigation.click_playground()

    def go_to_docs(self):
        return DashboardPage(self.page).navigation.click_docs()

    def go_to_community(self):
        return DashboardPage(self.page).navigation.click_community()

    def go_to_user_menu(self):
        return DashboardPage(self.page).navigation.expand_user_menu()

    def go_to_logout(self):
        return DashboardPage(self.page).navigation.expand_user_menu().click_logout()
