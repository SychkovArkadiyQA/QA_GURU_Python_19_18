import pytest
from selene import browser
#from demowebshop_test.utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser.config.base_url = 'https://demowebshop.tricentis.com/cart'
    browser.config.window_height = 1800
    browser.config.window_width = 1200

    yield browser

  #  attach.add_html(browser)
   # attach.add_screenshot(browser)
    #attach.add_logs(browser)

    #browser.quit()