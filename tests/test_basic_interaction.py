from pages.login_page import LoginPage


def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login('art.nagaytsev@gmail.com', 'suxrun-ryMpej-3jitho')  # TODO use password from secrets

    # assert dashboard_page
