import logging
import time

from resources.navigation import PageFactory

log = logging.getLogger(__name__)


def test_basic_interaction(login, page):
    """Test the basic interaction with the application.
    Steps:
    1. Login via the UI
    2. Send text via the chat UI
    3. Logout via the UI

    :param login: fixture
    """
    factory = PageFactory(page)

    # Login via the UI
    dashboard_page = login
    dashboard_page.verify_page()

    # Send text via the chat UI
    chat_page = factory.go_to_chat()
    chat_page.close_pop_up()
    chat_page.verify_page()  # TODO think about moving this to the navigation method or init
    chat_page.send_message("write fibonacci function")
    time.sleep(5)  # TODO replace with a wait for the response
    response = chat_page.get_messages()
    log.info(f"Response from the chat: {response}")
    assert response
