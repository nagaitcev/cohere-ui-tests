import configparser
import pytest
from .functions import login_to_page

# TODO use environment variables
config = configparser.ConfigParser()
config.read('secrets.ini')
USERNAME = config['DEFAULT']['USERNAME']
PASSWORD = config['DEFAULT']['PASSWORD']


@pytest.fixture(scope='module')
def login(driver):
    login_to_page(driver, USERNAME, PASSWORD)
    yield driver
    pass
    # logout_from_page(driver)