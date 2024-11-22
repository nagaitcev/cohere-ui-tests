import logging
import time

from resources.navigation import PageFactory

from .utils import create_unique_file

log = logging.getLogger(__name__)


def test_file_interaction(login, page):
    """Test the file interaction with the application.
    Steps:
    1. Login via the UI
    2. Upload a file via the UI
    3. Logout via the UI

    :param login: fixture
    """
    factory = PageFactory(page)

    # Login via the UI
    dashboard_page = login
    dashboard_page.verify_page()

    # Upload a file via the UI
    chat_page = factory.go_to_chat()
    chat_page.close_pop_up()
    chat_page.verify_page()  # TODO think about moving this to the navigation method or init
    test_file = create_unique_file("Write bubble sort function.")
    chat_page.upload_file([test_file])
    time.sleep(5)  # TODO replace with a wait for the response
    chat_page.verify_file_uploaded(test_file)
    chat_page.send_message("write function")
    time.sleep(5)  # TODO replace with a wait for the response
    response = chat_page.get_messages()
    log.info(f"Response from the chat: {response}")
    assert response
