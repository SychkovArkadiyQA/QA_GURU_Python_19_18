import allure
from selene import browser, have
from allure_commons.types import AttachmentType
import requests

from data.data import LOGIN, API_URL, WEB_URL, PASSWORD

class Authorization:

    def login_api(self):
        with allure.step("Login with API"):
            result = requests.post(
                url=API_URL + "/login",
                data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
                allow_redirects=False
        )
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        with allure.step("Get cookie from API"):
            self.cookie = result.cookies.get("NOPCOMMERCE.AUTH")

        with allure.step("Set cookie from API"):
            browser.open(WEB_URL)
            browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": self.cookie})
            browser.open(WEB_URL)

        with allure.step("Verify successful authorization"):
            browser.element(".account").should(have.text(LOGIN))

auth = Authorization()