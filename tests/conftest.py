import configparser
import datetime
import logging
import os

import pytest
from playwright.sync_api import sync_playwright

from .utils import login_to_page, logout_from_page

log = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--secrets-file",
        action="store",
        default="secrets.ini",
        help="Path to secrets file",
    )


@pytest.fixture(scope="session")
def secrets(request):
    secrets_file = request.config.getoption("--secrets-file")
    config = configparser.ConfigParser()
    config.read(secrets_file)

    if "credentials" not in config:
        raise ValueError("Section 'credentials' not found in secrets.ini")

    return {
        "username": config.get("credentials", "username"),
        "password": config.get("credentials", "password"),
    }


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="module")
def login(page, secrets):
    yield login_to_page(page, secrets["username"], secrets["password"])
    logout_from_page(page)


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler = logging.FileHandler("logs/test_log.log", mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    )
    logging.getLogger().addHandler(file_handler)

    logging.getLogger().info("Logging setup completed. Logs are saved to test_log.log.")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Get the result of the test and save it in the test_result attribute.
    """
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "test_result", rep)


@pytest.fixture(scope="function", autouse=True)
def capture_screenshot_on_failure(page, request):
    """
    Take a screenshot if the test failed.
    """
    yield
    test_result = getattr(request.node, "test_result", None)
    if test_result and test_result.failed:
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        test_name = request.node.name
        screenshot_path = os.path.join(
            screenshots_dir,
            f"{test_name}_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png",
        )

        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
