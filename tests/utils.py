import logging
import uuid

from pages.login_page import LoginPage
from resources.navigation import PageFactory

log = logging.getLogger(__name__)


def login_to_page(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(username, password)
    return dashboard_page


def logout_from_page(page):
    factory = PageFactory(page)
    factory.go_to_logout()
    return LoginPage(page)


def create_unique_file(file_content: str):
    unique_filename = f"test_file_{uuid.uuid4().hex}.txt"
    with open(unique_filename, "w") as file:
        file.write(file_content)
    log.info(f"File created: {unique_filename}")
    return unique_filename
