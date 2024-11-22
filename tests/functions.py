from pages.login_page import LoginPage
from resources.navigation import PageFactory


def login_to_page(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(username, password)
    return dashboard_page


def logout_from_page(page):
    factory = PageFactory(page)
    factory.go_to_logout()
    return LoginPage(page)
