from unittest import result
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure

from pages.cart_page import add_product_api

LOGIN = "Bond@example.com"
PASSWORD = "123456789"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"

ID_PRODUCT_1 = '74/1'
NAME_1 = 'Build your own expensive computer'




def test_login_api():
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    with step("Get cookie from API"):
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    with step("Set cookie from API"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))


@allure.story('Добавление и проверка товара в корзине')
def test_add_product():
    add_product_api.add_product(ID_PRODUCT_1).open_cart().check_add_product(NAME_1)

@allure.story('Добавление и проверка товара в корзине')
def test_add_product():
    add_product_api.add_product(ID_PRODUCT_1).open_cart().check_add_product(NAME_1)




